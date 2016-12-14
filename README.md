# Resume-Forwarder

A python Script to send job application resume to different companies.

This script will eliminate lot of time writing individual emails to all the firms i want to apply to.

this comes built in with the following features.

*Greetings and Salutation

*Opening Message

*Resume File Attached

*sends to Multiple Email with one line of code.

*gives live message when each email is sent.


*Improvements require in the future

*NO NEED TO DOWNLOAD 3rd PARTY LIBRARIES

# Before Using the Script
Before using the Script, enter your details in the following lines as mentioned

line 14 : your email address. eg: my.emailaddress@gmail.com

line 36 : password to the email address

line 20 : Subject you want to write

line 21 : Cover letter

line 25 : Attachment file name

line 26 : Attachment Location in out local computer

line 36 : The Email client you are using. the Default is set for gmail.

For yahoo :smtp.mail.yahoo.com 

For Office 360 : smtp.office365.com

For Outlook : smtp-mail.outlook.com
   
(THIS IS FOR THE CLIENT YOU ARE USING, NOT THE RECEIVER)


TIP:Go to the following page to turn down the security. (IF you cant turn this down(like i couldn't). Make a new Email address for this purpose.)

https://www.google.com/settings/security/lesssecureapps

# How to Use it:

in the terminal write the following code:

    python /file_location/file_name.py 4 email_1@address.com email_2@address.com email_3@address.com email_4@address.com

# Explanation of the terminal Line code:

1. python
2. File location and file name with extension
3. Number of addresses to send the email, here its 4 addresses
4. List of the 4 addresses you want to send the email, seperated by space

# Credits:
This work is based on the work done by @NaelShiab:
http://naelshiab.com/tutorial-send-email-python/
