# Zendesk Toolkit

#### Author(s): Leo Medalla, Shan Seneca

## Introduction

Welcome to the **Zendesk Toolkit User Manual**! This manual will guide you through the installation, setup, and usage of Zendesk Toolkit, a powerful Python script designed to assist Zendesk administrators in managing their ticket records efficiently. With the Zendesk Toolkit, you can easily back up and restore your Zendesk tickets, ensuring the safety and accessibility of your valuable customer support data, extending work lifetime, and provide counter-measures against sudden errors and accidents.

The Zendesk Toolkit consists of two main modules: the **Backup** module and the **Restore** module. The backup module enables you to download all the existing tickets from your Zendesk subdomain and store them in a JSON file that can be found in the root directory. On the other hand, the restore module allows you to upload previously backed up tickets back into your Zendesk subdomain, ensuring seamless data recovery and migration. Whether you need to back up your ticket data for safekeeping or restore previously saved tickets, the Zendesk Toolkit is here to streamline your workflow and ensure the smooth management of your Zendesk account.

## Getting Started

Please ensure that you have Python installed on your system. Additionally, make sure to review the **requirements.txt** file provided with the toolkit. This file lists the third-party modules required by the Zendesk Toolkit. To install these dependencies, you can run the **install_requirements.py** script, which will automatically download and set up the necessary modules. If you already have the required modules installed, you may skip this step.

Once you have completed the installation of the required dependencies, you are ready to begin using the Zendesk Toolkit. Simply run the **main.py** script, and the toolkit's console user interface will be launched, providing you with a convenient and intuitive way to manage your Zendesk ticket records.

> *Note: Please make sure not to change anything in the **MyZendeskApp.py** file to avoid errors. If you need any changes, please contact us or any assigned developer.*

## Usage

To effectively utilize the **Zendesk Toolkit**, follow the steps outlined below:

1. Launching the Zendesk Toolkit:
    - Open a terminal or command prompt
    - Navigate to the directory where the Zendesk Toolkit files are located
    - Run the **main.py** script by executing the following command:
        ```cmd
        python main.py
        ```
    - The toolkit's console user interface will open

<br>

2. Logging in to your Zendesk account:

    * **Subdomain**
        - Once the toolkit is opened, it will ask for the subdomain of your company:
            ```cmd
            Please enter your subdomain (e.g. https://{subdomain}.zendesk.com):
            ```
        - Only enter the subdomain of your company and not the entire website
        - Press **Enter**
        - This field will not allow an empty value and will prompt you again.

        <br>

        > *Note: There will be no input-checking if the entered subdomain is incorrect. If an event occurs, press `Ctrl + C` or `⌘ + C` to terminate the script and open the file again.* 

    <br>

    * **Account Email**
        - After entering the subdomain, you will be prompted to enter your account email:
            ```cmd
            Enter your account email:
            ```
        - Type in your email and press **Enter**.
        - This field will not allow an empty value and will prompt you again.

    <br>

    * **Account Password**
        - After entering the email, you will be prompted to enter your account password:
            ```cmd
            Enter your account password:
            ```
        - Type in your password and press **Enter**.
        - This field will not allow an empty value and will prompt you again.
        
        <br>

        > **Important**: Text that is typed in this field will not be seen in the console to ensure security when typing

    <br>

    * **Account Validation**
        - After entering the required fields, the program will test the validity of the credentials you entered.
        - If it fails the validation the program will terminate.
        - Run **main.py** again to retry.

<br>

3. Navigating the main menu:
    - Once you have successfully logged in, the program will present you three actions for you to choose:
        ```
        Choose actions:

        [1] Backup Tickets
        [2] Restore Tickets
        [3] Total Ticket Count
        [0] Exit

        Input:
        ```
    - Choose the number of the corresponding action that you want to execute `(e.g. Input: 1)`
    - This input field will not allow invalid inputs and will prompt you again. 

    <br>

    - **Backup Tickets**
        - This action will initiate a download sequence for all the tickets that is available in your subdomain.
        - A progress bar will show to indicate the progress of completion:
            ```cmd
            Backup progress: 200/300:  35%|█████▉           | 300/866 [00:06<00:12, 45.07 ticket(s)/s]
            ```
        > Note: This action will not backup tickets that are already existent in the **backup.json** file

    <br>

    - **Restore Tickets**
        - This action will initiate an upload sequence for all the tickets that were previously backed up by the toolkit.
        - A progress bar will show to indicate the progress of completion:
            ```cmd
            Restore progress: 0/100:  0%|                  | 300/866 [00:00<00:12, 0.0 ticket(s)/s]
            ```

        > Note: This action will not restore tickets existing in your Zendesk tickets 

    <br>

    > **Important**: Do not turn off your device when executing these actions until it is finished and do not cancel the actions in the middle of its progress to avoid anomalies.

    <br>

    - **Total Ticket Count**
        - This action will simply display the number of tickets that the toolkit has in the **backup.json** file.
        - Useful in validating **Backup Tickets**

## Package Files and Uses

### **backup.json** 

This file  is a JSON-formatted storage file used by **Zendesk Toolkit** to store all the backed up tickets from your Zendesk account. When you initiate the backup process using the toolkit, the script retrieves all existing tickets from your Zendesk subdomain and saves them in this file for future reference and restoration. 

The toolkit will always refer to the file name as **backup.json**. If you want it to be changed, contact us or any assigned developer. If the toolkit cannot find this file, it will create a new one.

The initial contents of this file must be the following to prevent incompatibilities in the script:
```json
[]
```

The structure of **backup.json** file is based on the formatting provided in Zendesk's API, ensuring that the backup contains the necessary details to restore the tickets accurately. Each ticket is represented as a JSON object within the file, containing various properties and their corresponding values.

The properties stored for each ticket may include:
- **Ticket ID**: A unique identifier assigned to each ticket in your Zendesk account.
- **Subject**: The subject or title of the ticket, providing a brief overview of its content.
- **Description**: The detailed description of the ticket, including any relevant information provided by the requester.
- **Requester**: The name or identifier of the user who submitted the ticket.
- **Status**: The current status of the ticket (e.g., open, pending, solved).
- **Priority**: The priority level assigned to the ticket (e.g., low, normal, high, urgent).
- **Tags**: Any tags associated with the ticket, enabling easier categorization and searchability.
- **Comments**: Additional comments, conversations, or interactions associated with the ticket, including timestamps and the users involved.

> **Important**: Remember to keep **backup.json** file in a secure location to prevent unauthorized access and ensure the integrity of your ticket data as this file can be easily accessed and manipulated.

### **install_requirements.py**

This file is a python script provided with **Zendesk Toolkit** that simplifies the process of installing the necessary third-party modules or dependencies required by the toolkit. This script automates the installation procedure, ensuring that all the required modules are correctly set up in your Python environment.

When you initially set up the **Zendesk Toolkit**, it is essential to review the **requirements.txt** file, which lists the specific third-party modules that the toolkit relies on. These modules are not part of the python standard library and may need to be installed separately.

> **Important**: This installation script only supports the following package managers: **pip**, **conda**. 
>
> If your package manager is not supported, please consult us or any assigned developer to install the requirements specified by the **requirements.txt** for you.

### **main.py**

This file is the main entry point of **Zendesk Toolkit**. It handles the entire program flow, providing a console user interface and orchestrating the functionality of the toolkit. The script interacts with the **MyZendeskApp.py** helper module to perform various operations related to ticket management in Zendesk.

### **MyZendeskApp.py**

This file is the most important file as this file contains the class functions that handles the backup and restore functionality of **Zendesk Toolkit**. Deletion of this file will permanently damage **Zendesk Toolkit**. 

### **requirements.txt**

This file lists the third-party modules required by the **Zendesk Toolkit**. Failure in installing these requirements will prevent the main script from functioning properly.

## Troubleshooting

Try these actions if you experience problems with **Zendesk Toolkit**:
- Ensure your Python version is greater than or equal to 3.0 by typing the command into your command prompt or shell:  
    ```cmd
    python --version
    ```
- Check if the requirements are installed using the command:
    ```cmd
    pip list | findstr {requirement_name}
    ```
    > Replace `{requirement_name}` with the actual requirement in the **requirements.txt** without the curly braces.

- Check the outmost symbol pair of **backup.json** if it is a pair of square brackets ( `[]` ). If it isn't, **Zendesk Toolkit** will likely throw an error since it will not function properly without the square brackets. To fix this, try to:
    - Delete all contents of **backup.json** and replace it with a pair of square brackets
    - Run the **Backup Tickets** action again to restore the contents

- Check if your Zendesk account enabled the API integration using email and password:
    - Go to the **Admin Center** of your administration
    - Click on the search bar on the left sidebar of the **Admin Center**
    - Search for **Zendesk API** and click on the result
    - Under **Settings**, check if **Password access** is enabled
    - Enable this toggle button if disabled
    - Make sure to disable this setting once you're done using with **Zendesk Toolkit**

## Feedback

- Have questions? Contact us at: [leomedalla1986@gmail.com](), [shnmyklsnc@gmail.com]()
- File a bug in [Github Issues](https://github.com/shshshshshan/ZendeskToolkit/issues)

## License

## [Apache License 2.0](https://github.com/shshshshshan/ZendeskToolkit/blob/master/LICENSE)
