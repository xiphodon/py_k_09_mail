#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/28 17:28
# @Author  : GuoChang
# @Site    : 
# @File    : py_k_09_email.py
# @Software: PyCharm

# !/usr/bin/env python
# coding:utf-8

import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


def email_text(message,mail_from,mail_from_psw,mail_to):
    """发送普通文字"""
    # 构造MIMEText对象,第一个参数就是邮件正文,第二个参数是MIME的subtype
    # 传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
    msg = MIMEText(message, 'plain', 'utf-8')  # message为传入的参数,为发送的消息.
    """msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8') """
    # 标准邮件需要三个头部信息： From, To, 和 Subject。
    msg['From'] = formataddr(["发送者昵称", mail_from])  # 显示发件人信息
    msg['To'] = formataddr(["接受者昵称", mail_to])  # 显示收件人信息
    msg['Subject'] = "测试邮件主题"  # 定义邮件主题

    try:
        # 创建SMTP对象
        server = smtplib.SMTP("smtp.sina.com", 25)
        # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
        server.set_debuglevel(1)
        # login()方法用来登录SMTP服务器
        server.login(mail_from, mail_from_psw)
        # sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
        server.sendmail(mail_from, [mail_to], msg.as_string())
        print("邮件发送成功!")
        server.quit()
    except smtplib.SMTPException as e:
        print("邮件发送失败!")
        print(e)


def email_file(message,mail_from,mail_from_psw,mail_to):
    """发送文字+附件"""

    # 附件使用 MIMEMultipart
    msg = MIMEMultipart()
    # 构造MIMEText对象,第一个参数就是邮件正文,第二个参数是MIME的subtype
    # 传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
    # 邮件正文是MIMEText:
    msg.attach(MIMEText(message, 'plain', 'utf-8')) # message为传入的参数,为发送的消息.
    """MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8') """
    # 标准邮件需要三个头部信息： From, To, 和 Subject。
    msg['From'] = formataddr(["发送者昵称", mail_from])  # 显示发件人信息
    msg['To'] = formataddr(["接受者昵称", mail_to])  # 显示收件人信息
    msg['Subject'] = "测试邮件主题"  # 定义邮件主题

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('python.jpg', 'rb') as f:
        # 设置附件的MIME和文件名，这里是jpg类型:
        mime = MIMEBase('image', 'jpg', filename='python.jpg')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='python.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    try:
        # 创建SMTP对象
        server = smtplib.SMTP("smtp.sina.com", 25)
        # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
        server.set_debuglevel(1)
        # login()方法用来登录SMTP服务器
        server.login(mail_from, mail_from_psw)
        # sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
        server.sendmail(mail_from, [mail_to], msg.as_string())
        print("邮件发送成功!")
        server.quit()
    except smtplib.SMTPException as e:
        print("邮件发送失败!")
        print(e)



def email_img(message,mail_from,mail_from_psw,mail_to):
    """发送文字+插图"""

    # 附件使用 MIMEMultipart
    msg = MIMEMultipart()
    # 构造MIMEText对象,第一个参数就是邮件正文,第二个参数是MIME的subtype
    # 传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
    # 邮件正文是MIMEText:
    msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
                        '<p><img src="cid:0"></p>' +
                        '</body></html>', 'html', 'utf-8')) # 此处填写好图片引用编号
    # 标准邮件需要三个头部信息： From, To, 和 Subject。
    msg['From'] = formataddr(["发送者昵称", mail_from])  # 显示发件人信息
    msg['To'] = formataddr(["接受者昵称", mail_to])  # 显示收件人信息
    msg['Subject'] = "测试邮件主题"  # 定义邮件主题

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('python.jpg', 'rb') as f:
        # 设置附件的MIME和文件名，这里是jpg类型:
        mime = MIMEBase('image', 'jpg', filename='python.jpg')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='python.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    try:
        # 创建SMTP对象
        server = smtplib.SMTP("smtp.sina.com", 25)
        # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
        server.set_debuglevel(1)
        # login()方法用来登录SMTP服务器
        server.login(mail_from, mail_from_psw)
        # sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
        server.sendmail(mail_from, [mail_to], msg.as_string())
        print("邮件发送成功!")
        server.quit()
    except smtplib.SMTPException as e:
        print("邮件发送失败!")
        print(e)


if __name__ == '__main__':
    mail_from = input("邮件发送者邮箱：")
    mail_from_psw = input("邮件发送者密码：")
    mail_to = input("邮件接收者：")
    # email_text("测试邮件的发送内容",mail_from,mail_from_psw,mail_to)
    # email_file("测试邮件的发送内容",mail_from,mail_from_psw,mail_to)
    email_img("测试邮件的发送内容",mail_from,mail_from_psw,mail_to)
