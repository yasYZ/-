import smtplib
import data
import datetime
from email.message import EmailMessage


category = data.in_cat
title = data.in_Name
number = data.in_Num

email = EmailMessage()

email['from'] = 'YazdanBaft.co@gmail.com'

email['to'] = 'yasinyazdani71@gmail.com'

email['subject'] = 'Learn Development for FREE!'


email.set_content(f"""
جناب محمد یزدانی عارف!

اضافه شد {datetime.datetime.today()} در تاریخ {category} به انبار {number} به تعداد {title} محصول 


**_______________________________________________________________________________**
this message for YazdanBaft Invenvtory application
CopyRighted by YazdanBaft
""")


def email_sender():
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:

        smtp.ehlo()

        smtp.starttls()

        smtp.login('YazdanBaft.co@gmail.com', 'xswrjyiydermfyji')

        smtp.send_message(email)

        print('email was sent!')
