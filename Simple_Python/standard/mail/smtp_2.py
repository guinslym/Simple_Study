#coding:utf-8
import smtplib
import email.utils
from email.mime.text import MIMEText

#创建信息
mail_server = "smtp.126.com"
mail_port="25"
username="example@126.com"
password="******"
msg = MIMEText("这是一份测试的邮件")
msg["To"] = email.utils.formataddr(('Recipient','yafeile@163.com'))
msg["From"] = email.utils.formataddr(('Niaoge',"zhuzhulang@126.com"))
msg["Subject"] = "A Test Email"
server=smtplib.SMTP(mail_server,mail_port)
server.login(username,password)
server.set_debuglevel(True)

try:
	server.sendmail("zhuzhulang@126.com",["yafeile@163.com,710642053@qq.com"],msg.as_string())
finally:
    server.quit()

