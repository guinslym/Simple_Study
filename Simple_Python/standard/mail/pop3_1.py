#coding:utf-8

import poplib

def sendMail():
     mail_server = "pop3.126.com"
     username="******@126.com"
     password="******"

     try:
          handle=poplib.POP3(mail_server)
          handle.set_debuglevel(1)
          handle.user(username)
          handle.pass_(password)
          welcome=handle.getwelcome()
          print welcome
          MsgNum,emailSize=handle.stat()
          print "email number is %d and size is %d" %(MsgNum,emailSize)
          for i in range(MsgNum):
               for piece in handle.retr(i+1)[1]:
                    if piece.startswith("Subject"):
                         title= "\t"+piece
                         print title
                         
          handle.quit()
          print "Get email success"
     except Exception, e:
          print "Get email failed because %s" % e

if __name__ == '__main__':
     sendMail()
