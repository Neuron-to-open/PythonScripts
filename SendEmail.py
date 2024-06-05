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
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import schedule

# 邮件服务器配置
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_password'


def generate_report():
    # 生成报告内容的函数
    report_content = f"Daily Report for {datetime.now().strftime('%Y-%m-%d')}\n"
    report_content += "This is an automatically generated report."
    return report_content


def send_email(report):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'neuronbyyi@gmail.com'
    msg['Subject'] = 'Daily Report'

    msg.attach(MIMEText(report, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, 'recipient_email@example.com', msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")


def job():
    report = generate_report()
    send_email(report)


# 设置每天定时发送邮件
schedule.every().day.at("08:00").do(job)

if __name__ == "__main__":
    schedule.run_pending()
