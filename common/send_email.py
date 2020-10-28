import smtplib
from email._header_value_parser import Header
from email.mime.text import MIMEText


def SendEmail(new_reportfile):
    """发送邮件"""
    msg_from = '15667021976@163.com'
    passward = 'aq243848459'  # 授权码
    to = ["243848459@qq.com"]  # 发送["***********@163.com","***********@qq.com","***********@qq.com"]
    Cc = ["243848459@qq.com"]  # 抄送
    receiver = to + Cc

    subject = '自动化测试结果'

    msg = MIMEText("正文内容","plain",'utf-8')
    msg['From'] = Header("自动化测试平台系统", 'utf-8')#msg['From'] = msg_from
    msg['Subject'] = subject
    msg['To'] = ";".join(to)  # Header("相关", 'utf-8')  #收件人
    msg["Cc"] = ";".join(Cc)  # 抄送人

    s = smtplib.SMTP('smtp.163.com', 25)   #smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(msg_from, passward)
    s.sendmail(msg_from, receiver, msg.as_string())


if __name__ == '__main__':
    path = 'F:\\v.txt'
    SendEmail(path)
