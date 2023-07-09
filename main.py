from MyZendeskApp import Zendesk
from getpass import getpass

def prompt_login() -> tuple[str, str]:
    username = password = None

    while not username:    
        username = input('Enter your account email: ')

        if username == '':
            print('\n* Email cannot be empty *')
            username = None

    while not password:    
        password = getpass('Enter your account password: ')

        if password == '':
            print('\n* Password cannot be empty *')
            password = None


    return username, password

def prompt_subdomain() -> str:
    subdomain = None

    while not subdomain:
        subdomain = input('Please enter your subdomain (e.g. https://{subdomain}.zendesk.com): ')

        if subdomain == '':
            print('\n * Please enter a valid subdomain *')
            subdomain = None

    return subdomain

def welcome():
    print('\nWelcome to Zendesk Toolkit\n')

def validate_credentials(zendesk: Zendesk, username: str, password: str):
    if not zendesk.login(username, password):
        print('Could not authenticate you')
        return False
    
    return True

def menu():
    print() # Indent
    print('Choose actions:\n', '[1] Backup Tickets', '[2] Restore Tickets', '[3] Total Ticket Count', '[0] Exit\n', sep='\n')

    choice = None

    while choice is None:

        try:
            choice = int(input('Input: '))

            if choice not in [0, 1, 2, 3]:
                choice = None
                raise ValueError

        except ValueError:
            print('* Invalid input *\n')

    return choice

def main():
    welcome()

    subdomain = prompt_subdomain()
    my_zendesk = Zendesk(subdomain)

    username, password = prompt_login()
    if not validate_credentials(my_zendesk, username, password):
        exit()

    choice = menu()

    if choice == 1:
        print('Please do not cancel this action or turn off your computer')
        my_zendesk.backup()
        print(f'Total tickets backed up: {my_zendesk.get_total_tickets()}')

    elif choice == 2:
        print('Please do not cancel this action or turn off your computer')
        my_zendesk.restore()
        print('Restore success')

    elif choice == 3:
        print(f'Total tickets backed up: {my_zendesk.get_total_tickets()}')

    elif choice == 0:
        exit()
    

if __name__ == '__main__':
    main()
    input('Press enter to exit...') 