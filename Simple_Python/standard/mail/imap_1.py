import imaplib,email
username="zhuzhulang@126.com"
password="030109"
handle=imaplib.IMAP4("imap.126.com",143)
handle.login(username,password)
handle.select("INBOX")
type,data=handle.search(None,"UNSEEN")
for num in data[0].split():
     type,data=handle.fetch(num,"RFC822")
     print "Message %s %s" % (num,data[0][1])
handle.close()