# -*- coding: gbk -*-
from HTMLTestRunner import  HTMLTestRunner
from BeautifulReport import BeautifulReport as bf
import unittest
from Test_login import Test_Login
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# suit = unittest.TestSuite()
# suit.addTest(Test_Login('test_LoginSccess1'))
# suit.addTest(Test_Login('test_LoginSccess2'))
# suit.addTest(Test_Login('test_LoginSccess3'))


# runner = HTMLTestRunner(
# #     stream=open("测试报告.html", "wb"),
# #     description="测试报告",
# #     title="unittest练习"
# # )
# # HTMLTestRunner()
# # runner.run(suit)


# run = bf(suit)  # 实例化BeautifulReport模块
# run.report(filename='test', description='商城shop登录模块自动化')

suit = unittest.TestSuite()
suit.addTest(Test_Login('test_LoginSccess1'))
suit.addTest(Test_Login('test_LoginSccess2'))
suit.addTest(Test_Login('test_LoginSccess3'))

def get_case_result():
    """ 获取测试用例报告 """
    file_path = 'result.html'
    with open(file_path, 'wb') as f:
        HTMLTestRunner(
            stream=f,
            description="测试报告",
            title="unittest练习"
         ).run(suit)
    f1 = open(file_path, 'r', encoding='utf-8')
    res = f1.read()
    f1.close()
    return res

def send_email():
    """ 发送邮件 """

    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1216557288@qq.com"  # 用户名
    mail_pass = "osmgfopououujaeg"  # 口令

    # 设置收件人和发件人
    sender = '1216557288@qq.com'
    receivers = ['1216557288@qq.com', '2812425823@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 创建一个带附件的实例对象
    message = MIMEMultipart()

    # 邮件主题、收件人、发件人
    subject = '请查阅--测试报告'  # 邮件主题
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("{}".format(sender), 'utf-8')  # 发件人
    message['To'] = Header("{}".format(';'.join(receivers)), 'utf-8')  # 收件人

    # 邮件正文内容 html 形式邮件
    send_content = get_case_result()  # 获取测试报告
    html = MIMEText(_text=send_content, _subtype='html', _charset='utf-8')  # 第一个参数为邮件内容

    # 构造附件
    att = MIMEText(_text=send_content, _subtype='base64', _charset='utf-8')
    att["Content-Type"] = 'application/octet-stream'
    file_name = 'result.html'
    att["Content-Disposition"] = 'attachment; filename="{}"'.format(file_name)  # # filename 为邮件附件中显示什么名字
    message.attach(html)
    message.attach(att)

    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtp_obj.login(mail_user, mail_pass)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        smtp_obj.quit()
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == '__main__':
    send_email()
