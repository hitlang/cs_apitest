# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

import smtplib
import threading
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

from config import global_config

report_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "report"))
report_file = os.path.abspath(os.path.join(report_dir, "report.html"))


class Email:
    def __init__(self):
        global host, user, password, port, sender, title, receiver
        host = "smtp.163.com"
        user = "easyme2046@163.com"
        password = "RLZZBCQDMHHVXBTT"
        sender = "easyme2046@163.com"
        self.receiver = [i  for i in  global_config.get_email_receivers().split(",")]

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.subject = "dbshop13版本。移动端接口测试报告" + " " + date

        self.msg = MIMEMultipart('related')
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiver)

        with open(report_file, encoding="utf-8") as f:
            content = f.read()

        content_plain = MIMEText(content, 'html', 'utf-8')

        self.msg.attach(content_plain)


    def send_email(self):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.login(user, password)
            smtp.sendmail(sender, self.receiver, self.msg.as_string())
            smtp.quit()
        except Exception as ex:
            pass

#
# class MyEmail:
#     email = None
#     mutex = threading.Lock()
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def get_email():
#         if MyEmail.email is None:
#             MyEmail.mutex.acquire()
#             MyEmail.email = Email()
#             MyEmail.mutex.release()
#         return MyEmail.email


if __name__ == "__main__":
    # email = MyEmail.get_email()
    email = Email()
    email.send_email()
