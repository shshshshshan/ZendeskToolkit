import asyncio
import requests
import json
import time
from tqdm import tqdm
from typing import Final
import os

BACKUP_FILE_NAME = 'backup'

class Zendesk:

    def __init__(self, subdomain: str) -> None:
        self.subdomain = subdomain
        self.domain = f'https://{subdomain}.zendesk.com'

        self.__initBackupFile__()

    def __initBackupFile__(self) -> None:
        if not os.path.exists(f'{BACKUP_FILE_NAME}.json'):
            with open(f'{BACKUP_FILE_NAME}.json', 'w', encoding='utf-8') as f:
                json.dump([], f, indent=2)
        else:
            try:
                with open(f'{BACKUP_FILE_NAME}.json', 'r', encoding='utf-8') as f:
                    content = json.load(f)

                    if type(content) != list:
                        raise Exception(f"{BACKUP_FILE_NAME}.json expected a container of <class 'list'>, got {type(content)} instead.")
                    
            except json.decoder.JSONDecodeError:
                with open(f'{BACKUP_FILE_NAME}.json', 'w', encoding='utf-8') as w:
                    json.dump([], w, indent=2)
    
    def login(self, username, password) -> bool:
        session = requests.Session()
        session.auth = username, password

        # Test endpoint to validate login
        url = f'{self.domain}/api/v2/tickets/count'
        response = session.get(url)

        if response.status_code == 401:
            return False
        
        self.session = session
        return True

    def backup(self) -> None:
        asyncio.run(self.__backupAsyncInit__())

    def restore(self) -> None:
        asyncio.run(self.__restoreAsyncInit__())

    def get_total_tickets(self) -> int:
        with open(f'{BACKUP_FILE_NAME}.json', mode='r', encoding='utf-8') as f:
            contents = json.load(f)

        return len(contents)

    # Bulk Download Data
    async def __backupAsync__(self, progress_bar: tqdm) -> None:

        # API Endpoint for getting bulk tickets
        url = f'{self.domain}/api/v2/tickets.json?sort_by=created_at&sort_order=desc&page[size]=100'

        contents = None
        comments = []

        # Existing backed up tickets
        with open(f'{BACKUP_FILE_NAME}.json', mode='r', encoding='utf-8') as f:
            contents = json.load(f)

        # Progress bar info
        total_tickets = 0
        progress_bar.set_description(f'Starting... ')

        existing_ticket_ids = {content['id'] for content in contents}

        while url:
            
            response = self.session.get(url)

            if response.status_code == 429:
                print('Rate limited, please wait')
                time.sleep(int(response.headers['retry-after']))
                continue

            if response.status_code != 200:
                print(f'Error with status code {response.status_code}')
                exit()

            data = response.json()

            # Update progress bar
            total_tickets += len(data['tickets'])
            progress_bar.set_description(f'Backup progress: {progress_bar.n}/{total_tickets}')

            # Separate download for the comments (couldn't find any side-loading guide for comments)
            for ticket in data['tickets']:
                if ticket['id'] not in existing_ticket_ids:
                    url = f'{self.domain}/api/v2/tickets/{ticket["id"]}/comments'
                    response = self.session.get(url)
                    comments.append(response.json()['comments'])
                    time.sleep(.5)
                    contents.append(ticket)
                    existing_ticket_ids.add(ticket['id'])
                    
                    progress_bar.set_description(f'Backup progress: {progress_bar.n}/{total_tickets}')
                progress_bar.update()

            if data['meta']['has_more']:
                url = data['links']['next']
            else:
                url = None

            # Guard for the API call limit
            time.sleep(.5)

        # Append the comment into its respective ticket
        for ticket, comment in zip(contents, comments):
            ticket['comments'] = comment

        with open(f'{BACKUP_FILE_NAME}.json', mode='w', encoding='utf-8') as f:
            json.dump(contents, f, sort_keys=True, indent=2)

    async def __backupAsyncInit__(self) -> None:

        url = f'{self.domain}/api/v2/tickets/count'
        response = self.session.get(url)

        if response.status_code != 200:
            print(f'Error with status code {response.status_code}, {response.text}')
            exit()

        data = response.json()
        total_tickets = data['count']['value']

        with tqdm(total=total_tickets, unit=' ticket(s)', ncols=90) as progress_bar:
            await self.__backupAsync__(progress_bar)

    # Restore data
    async def __restoreAsync__(self, progress_bar: tqdm, contents) -> None:
        progress_bar.set_description(f'Starting... ')

        # Getting existing tickets in the subdomain

        # API Endpoint for getting bulk tickets
        url = f'{self.domain}/api/v2/tickets.json?sort_by=created_at&sort_order=desc&page[size]=100'

        existing_tickets = []

        while url:
            
            response = self.session.get(url)

            if response.status_code == 429:
                print('Rate limited, please wait')
                time.sleep(int(response.headers['retry-after']))
                continue

            if response.status_code != 200:
                print(f'Error with status code {response.status_code}')
                exit()

            data = response.json()
            existing_tickets.extend(data['tickets'])

            if data['meta']['has_more']:
                url = data['links']['next']
            else:
                url = None

            # Guard for the API call limit
            time.sleep(.5)

        existing_ticket_ids = {ticket['id'] for ticket in existing_tickets}

        # Importing

        # API endpoint to import tickets
        url = f'{self.domain}/api/v2/imports/tickets/create_many?archived_immediately=false'

        # URL and ID is auto-generated while 
        # Satifaction rating causes an error if value is copied
        unwanted_keys = ['url', 'satisfaction_rating', 'id']

        headers = {
            "Content-Type": "application/json",
        }

        # Page size or limit per batch
        LIMIT: Final = 100

        for i in range(0, len(contents), LIMIT):

            progress_bar.set_description(f'Restore progress: {progress_bar.n}/{progress_bar.total}')

            batch = contents[i:i + min(len(contents), LIMIT)]

            # Original length before filtering for existing tickets
            batch_lenth = len(batch)

            batch = [item for item in batch if item['id'] not in existing_ticket_ids]

            if len(batch) == 0:

                # Update progress bar
                progress_bar.update(batch_lenth)

                time.sleep(.5)
                continue

            batch = [{key : value for key, value in item.items() if key not in unwanted_keys} for item in batch]

            payload = { 'tickets' : batch }
            response = self.session.post(url, headers=headers, json=payload)

            if response.status_code == 429:
                print('Rate limited, please wait')
                time.sleep(int(response.headers['retry-after']))
                continue

            elif response.status_code == 201:
                print('Imported')
                continue

            elif response.status_code != 200:
                print(f'Error with status code {response.status_code}, {response.text}')
                exit()

            # Guard against rate limit
            time.sleep(1)

            # Update progress bar
            progress_bar.update(batch_lenth)

    async def __restoreAsyncInit__(self):

        with open(f'{BACKUP_FILE_NAME}.json', mode='r', encoding='utf-8') as f:
            contents = json.load(f)

        with tqdm(total=len(contents), unit=' ticket(s)', ncols=90) as progress_bar:
            await self.__restoreAsync__(progress_bar, contents)



if __name__ == '__main__':
    print('This is not a script')


    # TODO: 
    # Make program flow for login