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
# #     stream=open("���Ա���.html", "wb"),
# #     description="���Ա���",
# #     title="unittest��ϰ"
# # )
# # HTMLTestRunner()
# # runner.run(suit)


# run = bf(suit)  # ʵ����BeautifulReportģ��
# run.report(filename='test', description='�̳�shop��¼ģ���Զ���')

suit = unittest.TestSuite()
suit.addTest(Test_Login('test_LoginSccess1'))
suit.addTest(Test_Login('test_LoginSccess2'))
suit.addTest(Test_Login('test_LoginSccess3'))

def get_case_result():
    """ ��ȡ������������ """
    file_path = 'result.html'
    with open(file_path, 'wb') as f:
        HTMLTestRunner(
            stream=f,
            description="���Ա���",
            title="unittest��ϰ"
         ).run(suit)
    f1 = open(file_path, 'r', encoding='utf-8')
    res = f1.read()
    f1.close()
    return res

def send_email():
    """ �����ʼ� """

    # ������ SMTP ����
    mail_host = "smtp.qq.com"  # ���÷�����
    mail_user = "1216557288@qq.com"  # �û���
    mail_pass = "osmgfopououujaeg"  # ����

    # �����ռ��˺ͷ�����
    sender = '1216557288@qq.com'
    receivers = ['1216557288@qq.com', '2812425823@qq.com']  # �����ʼ���������Ϊ���QQ���������������

    # ����һ����������ʵ������
    message = MIMEMultipart()

    # �ʼ����⡢�ռ��ˡ�������
    subject = '�����--���Ա���'  # �ʼ�����
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("{}".format(sender), 'utf-8')  # ������
    message['To'] = Header("{}".format(';'.join(receivers)), 'utf-8')  # �ռ���

    # �ʼ��������� html ��ʽ�ʼ�
    send_content = get_case_result()  # ��ȡ���Ա���
    html = MIMEText(_text=send_content, _subtype='html', _charset='utf-8')  # ��һ������Ϊ�ʼ�����

    # ���츽��
    att = MIMEText(_text=send_content, _subtype='base64', _charset='utf-8')
    att["Content-Type"] = 'application/octet-stream'
    file_name = 'result.html'
    att["Content-Disposition"] = 'attachment; filename="{}"'.format(file_name)  # # filename Ϊ�ʼ���������ʾʲô����
    message.attach(html)
    message.attach(att)

    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(mail_host, 25)  # 25 Ϊ SMTP �˿ں�
        smtp_obj.login(mail_user, mail_pass)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        smtp_obj.quit()
        print("�ʼ����ͳɹ�")

    except smtplib.SMTPException:
        print("Error: �޷������ʼ�")


if __name__ == '__main__':
    send_email()
