from datetime import datetime
from email.message import EmailMessage
import random
import smtplib
from constants import *


from datetime import date, datetime


#obtenemos los datos de la fecha de hoy y hora
today=datetime.today()


# (0 = Monday, 1 = Tuesday, ..., 6 = Sunday), quiero mandar un correo todos los dias, asi que creo lista de dias
my_day=[0, 1, 2, 3, 4, 5, 6]


#recorro la lista
for dia in my_day:
        
    # Compruebo si el día de la semana actual es el mismo que my_day y envio el correo
    if today.weekday()==dia:
            
            
        with open('quotes.txt', encoding='utf-8') as phrase:
            # creamos una lista que contiene cada linea de nuestro archivo
            phrase_list = phrase.readlines()

            # Escogemos aleatoriamente una frase de nuestra nueva lista
            random_phrase = random.choice(phrase_list)

        # TODO: enviaremos nuestra nueva quote a nuestro email
        my_email = EMAIL
        password = PASSWORD

        # creamos instancia de EmailMessage()
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

                


        #mandamos el correo con nuestros datos
        #creamos instancia de smtplib
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            
            #  TLS (Transport Layer Security), usamos esta funcion para encriptar nuestro msj y para una conexion segura
            connection.starttls()
            
            
            #ingresamos nuestro correo y contrasena a la funcion login
            connection.login(my_email, password)
            
            
            #enviamos nuestro correo
            connection.send_message(msg)

        