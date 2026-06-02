'''
SMTP (Simple Mail Transfer Protocol)
------------------------------------
--> This is used to send emails from server to another...

Note:
----
1.SMTP SSL Port
---------------
465

2.SMTP TLS port
---------------
587

import smtplib

EmailMessage Class
------------------
msg['Subject'] = 'SMTP ON Mail'
msg['From'] = 'Sender@mail.com'
msg['To'] = 'Receiver@mail.com'


import smtplib
from email.message import EmailMessage
sender = 'peyyalakaushik21@gmail.com'
password = 'swbvugfuckxpxliy'
msg = EmailMessage()

msg['Subject'] = 'Welcome Mail'
msg['From'] = 'peyyalakaushik21@gmail.com'
msg['To'] = 'jayrajpathangay@gmail.com'

msg.set_content('jay')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()

'''

import smtplib
from email.message import EmailMessage
sender = 'peyyalakaushik21@gmaill.com'
password = 'qulzkcperiavynzu'
msg = EmailMessage()
receiver = ['jayrajpathangay@gmail.com','rajasainikhil.7@gmail.com']
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
for email in receiver:
    msg = EmailMessage()
    msg['subject'] = 'Welcome Mail'
    msg['From'] = sender
    msg['To'] = email
    msg.set_content('Hello Jay')
    server.send_message(msg)
server.quit()
















