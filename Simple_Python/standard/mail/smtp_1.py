#coding:utf-8

import smtplib

def sendMail(mail_to):
	mail_server = "smtp.163.com"
	mail_port="25"
	username="example@163.com"
	password="******"
	mail_title="python test"
	mail_content="This is a test from python for sending email"
	if type(mail_to)==str:
		mail_list=mail_to.split(";")
	elif type(mail_to)==list:
		mail_list=mail_to
	else:
		print "你输入的收件人有误"

	try:
		handle=smtplib.SMTP(mail_server,mail_port)
		handle.login(username,password)
		msg="From:%s\n To:%s\nContent-type:text/html;charset=gb2312\nSubject:%s\n\n%s" %("bird",";".join(mail_list),mail_title,mail_content)
		handle.sendmail(username,mail_list,msg)
		handle.close()
		print "Send email success"
	except Exception, e:
		print "Send email failed because %s" % e

if __name__ == '__main__':
	sendMail("zhuzhulang@126.com")