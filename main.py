from datetime import datetime
from email.message import EmailMessage
import random
import smtplib
from constants import *
import schedule

from datetime import date, datetime


# Get today's date and time
today = datetime.today()


# (0 = Monday, 1 = Tuesday, ..., 6 = Sunday), I want to send an email every day, so I create a list of days
my_day = [0, 1, 2, 3, 4, 5, 6]


# Iterate through the list
for dia in my_day:
        
    # Check if the current weekday is the same as my_day and send the email
    if today.weekday() == dia:
            
        with open('bibemessage.txt', encoding='utf-8') as phrase:
            # Create a list containing each line of our file
            phrase_list = phrase.readlines()

            # Randomly choose a phrase from our new list
            random_phrase = random.choice(phrase_list)

        # TODO: Send our new quote to our email
       
        my_email = EMAIL
        password = PASSWORD

        # List of emails
        email_list = [my_email]
        
        # Create an instance of EmailMessage()
        msg = EmailMessage()

        msg['Subject'] = "Motivation Quote"
        msg['From'] = my_email
        msg['to'] = 'ricardoantoniogomezvillalobos@gmail.com'
        msg.set_content(f'''
        <!DOCTYPE html>
            <html>
            <head>
                <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style type="text/css">
                h1{{font-size:56px}}
                h2{{font-size:28px;font-weight:900}}
                p{{font-weight:100}}
                td{{vertical-align:top}}
                #email{{margin:auto;width:600px;background-color:#fff}}
                </style>
            </head>
            <body bgcolor="#F5F8FA" style="width: 100%; font-family:Lato, sans-serif; font-size:18px;">
            <div id="email">
                <table role="presentation" width="100%">
                    <tr>
                        <td bgcolor="#00A4BD" align="center" style="color: white;">
                            <h1>{random_phrase}</h1>
                        </td>
                </table>
                
            </div>
            </body>
            </html>
        ''', subtype='html')

        
        # Send the email with our data
        # Create an instance of smtplib
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            
            # TLS (Transport Layer Security), use this function to encrypt our message and for a secure connection
            connection.starttls()
            
            
            # Enter our email and password into the login function
            connection.login(my_email, password)
            
            
            # Send our email
            connection.send_message(msg)





