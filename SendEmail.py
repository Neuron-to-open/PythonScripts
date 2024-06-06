# /****************************************************************************
# * Author: Neuron-to-open
# * Date: 2024/6/2
# * Python : 3.11
# * 系统版本： Windows 11 家庭版 20H2
# * IDE: Pycharm
# * 编程语言: Python
# * =========== ====== ===== ==============================================
# * @Copyright (C) Yijiayi All Rights reserved
# *****************************************************************************/
# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 15:00
# @Author  : hang1720
# @Site    :
# @File    : send_email_code.py
# @Software: PyCharm

import random
# 发送纯文本
import smtplib
# 发送标题
# 邮件正文
from email.mime.text import MIMEText

# 生成一个6位的随机验证码，并转换为字符串格式
code = random.sample(list(range(1, 101)), 6)
code = list(map(lambda x: str(x), code))
code = ' '.join(code)

# 定义发送邮件的函数
# 参数:
# user: 发件人的邮箱用户名
# pwd: 发件人的邮箱密码
# sender: 发件人的邮箱地址
# receiver: 收件人的邮箱地址列表
# content: 邮件的正文内容
# title: 邮件的标题
# print(sim)
def sendMail(user, pwd, sender, receiver, content, title):
    # 邮件发送的主机
    mail_host = "smtp.qq.com"  # qq的SMTP服务器
    # 创建一个MIMEText对象，设置邮件内容、格式和编码
    # 第一部分：准备工作
    # 1.将邮件的信息打包成一个对象
    message = MIMEText(content, "plain", "utf-8")  # 内容，格式，编码
    # 设置邮件的发件人和收件人
    # 2.设置邮件的发送者
    message["From"] = sender
    # 3.设置邮件的接收方
    # message["To"] = receiver
    # join():通过字符串调用，参数为一个列表
    message["To"] = ",".join(receiver)
    # 设置邮件的标题
    # 4.设置邮件的标题
    message["Subject"] = title

    # 尝试发送邮件
    # 第二部分：发送邮件
    try:
        # 初始化SMTP_SSL对象，登录邮箱
        # 1.启用服务器发送邮件
        # 参数：服务器，端口号
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        # 2.登录邮箱进行验证
        # 参数：用户名，授权码
        smtpObj.login(user, pwd)
        # 3.发送邮件
        # 参数：发送方，接收方，邮件信息
        smtpObj.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")
    except:
        print('邮件发送失败')

    # 等待用户输入验证码，并验证输入的验证码是否正确
    code_1 = input('请输入您收到的验证码：')
    if code == code_1:
        print('恭喜您输入的正确')

# 主程序入口
if __name__ == "__main__":
    # 邮箱用户名、密码、发件人和收件人
    mail_user = "xxx@qq.com"
    mail_pwd = "xxxx"
    mail_sender = "xxx@qq.com"
    shoujian = "xxx@163.com"
    # csr = input('请输入抄送人：')
    # receivers = csr.split(' ')
    mail_receiver = shoujian
    print(mail_receiver)

    # 邮件内容和标题
    email_content = "人生苦短，我用Python ，您的验证码为：%s" % code
    email_title = "AID人工智能"

    # 调用函数发送邮件
    sendMail(mail_user, mail_pwd, mail_sender,
             mail_receiver, email_content, email_title)





