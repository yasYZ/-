import smtplib
import datetime
import data
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'YazdanBaft.co@gmail.com'
email['to'] = 'yasinyazdani71@gmail.com'
email['subject'] = 'Learn Development for FREE!'

email.set_content(f"""
جناب محمد یزدانی عارف!

اضافه شد {datetime.datetime.today()} در تاریخ {data.in_cat} به انبار {data.in_Num} به تعداد {data.in_Name} محصول

**_______________________________________________________________________________**
this message for YazdanBaft Inventory application
CopyRighted by YazdanBaft
""")


def email_sender():
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('YazdanBaft.co@gmail.com', 'xswrjyiydermfyji')
        smtp.send_message(email)
        print('Email was sent!')
