# Zendesk Toolkit 2.0

#### Authors: Leo Medalla, Shan Seneca

## Introduction

Welcome to the **Zendesk Toolkit User Manual**! This manual will guide you through the installation, setup, and usage of Zendesk Toolkit, a powerful software designed to assist Zendesk administrators in managing their Zendesk records efficiently. With the Zendesk Toolkit, you can easily back up and restore your Zendesk records, ensuring the safety and accessibility of your valuable customer support data, extending work lifetime, and provide counter-measures against sudden errors and accidents.

The Zendesk Toolkit consists of three main sections: **Homepage**, **Toolkit**, and **Settings** section. The **Homepage** section entails the overview of your relevant account information, recent imports and exports, and a dashboard to keep track of your back up status and the total number of records backed up. The **Toolkit** section is the highlight of the software where it contains an import and export button for each of the Zendesk records: **Users**, **Tickets**, and **Organizations**. For now, the toolkit is limited to these records only and will be improved to handle more records if needed in the future development. The **import** module enables you to download all the existing records from your Zendesk subdomain and store them in a JSON file that can be found in the directory stated in the settings section. On the other hand, the **export** module allows you to upload previously backed up tickets back into your Zendesk subdomain, ensuring seamless data recovery and migration. Whether you need to back up your ticket data for safekeeping or restore previously saved tickets, the Zendesk Toolkit is here to streamline your workflow and ensure the smooth management of your Zendesk account. The last section, **Settings**, contain only basic functionalities: cache clearing, changing default path of the record files, reporting bugs and errors.

## System Requirements

Currently, the toolkit only runs in Windows operating systems, preferrably latest windows versions. The application will require you to run it as administrator. The toolkit will prompt you upon opening it.

## Installation

In this repository, you will find an MSI (Microsoft Installer) setup file for the toolkit. Download and run this file to initialize the installer wizard. Upon running the microsoft installer, it will ask you to define an installation location and the installation option to install it in your own computer account or anyone. After clicking next, the wizard will start the installation process which will then create a desktop shortcut of the app.

## Usage

To effectively utilize the **Zendesk Toolkit**, follow the steps outlined below:

1. Launching the Zendesk Toolkit:
    - Open the toolkit by either launching the shortcut icon in the desktop or locating the executable file in the location you set in the installation.
    - There will be an authorization prompt wherein it will ask you to allow administrator access to the application.

    <br>

    > *Note: Administator access is required to allow the application to make changes to the records inside the default location (Program Files x86) which requires administrator access.*

<br>

2. Logging in to your Zendesk account:

    * **Subdomain**
        - Once the toolkit is opened, it will ask for the subdomain of your company.
        - Only enter the subdomain of your company and not the entire website url.
        - Click **Next** or press the **Enter** to proceed.
        - This field will not allow an empty value and will prevent you from proceeding.

        <br>

        > *Note: There will be no input-checking if the entered subdomain is incorrect. Please make sure to review your input.*
    <br>

    * **Account Credentials**
        - After entering the subdomain, you will be prompted to enter your account email and password.
        - These fields have input checking and will prevent you from proceeding if your input does not follow proper syntax in the email.

    <br>

    * **Account Validation**
        - After entering the required fields, the program will test the validity of the credentials you entered.
        - If it fails the validation the program will display an error message.

        <br>

        > *Note: The error message is intended to be vague to prevent bad actors or hackers to obtain clues to exploiting your account.*

<br>

3. Navigating the application:
    - Once you have successfully logged in, you will be redirected to the homepage where you can navigate through the sections on the navigation bar on the left.

    <br>

    - **Homepage**
        - This section features three main functions: **account information**, **overview**, and **dashboard**.

        <br>

        - **Account Information**
            - Shows you the relevant information of your account such as **Name**, **Role**, **Email**, and **Subdomain**.
            
            <br>

            > *Note: Information displayed here is readonly.*
        
        - **Overview**
            - Shows you the recent import/export information for each Zendesk record.

        <br>

        - **Dashboard**
            - Shows you the total number of backed up records and the back up status.
            - The back up status will display **Backed up** if you have imported or backed up your Zendesk records for the current day.
            - The back up status will display **Not backed up** if you have not imported or backed up your Zendesk records for the current day.
            - The total number of backed up records will remain unchanged and bases the count in the back up file that can be found in the root directory of the file.

    <br>

    - **Toolkit**
        - This section features the main module of the application where each Zendesk record comprise its own import and export functionality.
        - Each Zendesk record is separated with tabs, each tab contains identical functions: import, export, syncing of online and local counts, opening the record files and a view of the recent import and recent export date time.

        - **Import**
            - This action will initiate a download sequence for all the corresponding records that is available in your subdomain.
            - A progress bar will show to indicate the progress of completion.

            <br>

            > *Note: This action will not back up records that are already existent in the back up file.*


        - **Restore Tickets**
            - This action will initiate an upload sequence for all the records that were previously backed up by the toolkit.
            - A progress bar will show to indicate the progress of completion.

            <br>

            > *Note: This action will not restore records existent in your Zendesk subdomain.*

        <br>

        > **Important**: Do not turn off your device when executing these actions until it is finished and do not cancel the actions in the middle of its progress to avoid anomalies.
    
    <br>

    - **Settings**
        - This section contains some basic settings for the Zendesk toolkit.
        - These are the **Logout**, **Change Theme**, **Clear Cache**, **Change Default File Path**, and **About**.

        <br>

        - **Logout**
            - Ends your current session with the toolkit.
            - A **Remember Me** feature is offered in the login interface to ease your logging sessions.

        <br>

        - **Change Theme** (*Currently disabled*)
            - Changes the main color theme of the application

        <br>

        - **Clear Cache**
            - This will reset the **recent import** and **recent export** data in your records.

        <br>

        - **Change Default File Path**
            - This will move your records to the path specified.
            - This will not move all the Zendesk Toolkit's program files, only the records. 

        <br>

        - **About**
            - Contains the developers' contact information, a **Report A Bug** link where it will open a browser for you and redirects you to [**Github Issues**](https://github.com/shshshshshan/ZendeskToolkit/issues) and a link to the license of the program where it will also open a browser for you and redirects you.


## Uninstalling

There are two ways to uninstall the Zendesk toolkit:

1. Going to your settings and search for **Add or remove programs**, locate the application and then simply uninstall it.

2. Locate the installation directory you set in the installation process, run the microsoft installer again, select "Remove the program" in the two selections.

<br>

> *Note: The uninstallation process will not automatically remove the record files and cache files.*

## Troubleshooting

Try these actions if you experience problems with **Zendesk Toolkit**:
- Try not to tamper with the records if the Zendesk toolkit is still running or you are still going to use it to import/export records as this can cause errors.
- Check the outmost symbol pair of the back up file of your records if it is a pair of curly braces ( `{}` ). If it isn't, **Zendesk Toolkit** will likely throw an error since it will not function properly without the curly braces. To fix this, try to delete the file itself and use the **import** action of the corresponding records as this will restore it automatically.
- Check if your Zendesk account enabled the API integration using email and password:
    - Go to the **Admin Center** of your administration
    - Click on the search bar on the left sidebar of the **Admin Center**
    - Search for **Zendesk API** and click on the result
    - Under **Settings**, check if **Password access** is enabled
    - Enable this toggle button if disabled
    - Make sure to disable this setting once you're done using with **Zendesk Toolkit**
- Ensure you have a reliable internet connection as this is crucial to the application, the program cannot function well without internet connection but is not fully online as the records will not be loaded if you log in your account to a different device.

## Feedback

- Have questions? Contact us at: [leomedalla1986@gmail.com](), [shnmyklsnc@gmail.com]()
- File a bug in [Github Issues](https://github.com/shshshshshan/ZendeskToolkit/issues)

## License

## [Apache License 2.0](https://github.com/shshshshshan/ZendeskToolkit/blob/master/LICENSE)
