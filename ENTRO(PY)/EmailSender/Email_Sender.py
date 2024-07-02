# go over to your gmail account and setup 2-factor auth
# generate app password
# create a function to send the email

from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'matheuspina1095@gmail.com'
email_password = password


email_receiver = 'xemicig862@elahan.com'

subject = "Die, Bitch"
body = """
FUCK YOU
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())