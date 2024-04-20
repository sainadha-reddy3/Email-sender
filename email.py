from email.message import EmailMessage
from email import password
import ssl
import smtplib

email_sender = 'sainadhareddy10@gmail.com'
email_password = password

email_receiver = 'sainadhareddy9@gmail.com'
subject = "dont forget to logout"
body = """
when you use the mail, please dont forget to logout
"""
em = EmailMessage()
em['from'] = email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender , email_receiver , em.as_string())




