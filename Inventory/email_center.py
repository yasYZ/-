import smtplib
import datetime
from email.message import EmailMessage


def email_input_sender(name, number, category):
    """send a email with detail for input items"""
    port = 587  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "yazdanbaft.co@gmail.com"  # Enter your address
    receiver_email = "yasinyazdani71@gmail.com"  # Enter receiver address
    password = "xswrjyiydermfyji"

    message = EmailMessage()
    message.set_content(f"""
    جناب محمد یزدانی عارف!
    
    محصول {name} به تعداد {number} به انبار {category} در تاریخ {datetime.datetime.today()}اضافه شد
    
    **_______________________________________________________________________________**
    this message for YazdanBaft Inventory application
    CopyRighted by YazdanBaft
    """)
    message['Subject'] = 'Subject of your email'
    message['From'] = sender_email
    message['To'] = receiver_email

    with smtplib.SMTP(host=smtp_server, port=port) as server:
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)
        print('Email was sent!')


def email_export_sender(name, number):
    """send a email with detail for export items"""
    port = 587  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "yazdanbaft.co@gmail.com"  # Enter your address
    receiver_email = "yasinyazdani71@gmail.com"  # Enter receiver address
    password = "xswrjyiydermfyji"

    message = EmailMessage()
    message.set_content(f"""
جناب محمد یزدانی عارف!
    
محصول {name} به تعداد {number} در تاریخ {datetime.datetime.today()} خارج شد    
**_______________________________________________________________________________**
this message for YazdanBaft Inventory application
CopyRighted by YazdanBaft
""")
    message['Subject'] = 'Subject of your email'
    message['From'] = sender_email
    message['To'] = receiver_email

    with smtplib.SMTP(host=smtp_server, port=port) as server:
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)
        print('Email was sent!')
