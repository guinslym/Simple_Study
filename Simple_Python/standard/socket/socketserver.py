#coding=utf-8
import socket

host=""
port=51423

#step 1(create the socket object)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#step 2(set the socket option)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

#step 3(bind to a port and interface)
s.bind((host,port))
print "Waiting for connecting..."

#step 4(Listen for connections)
s.listen(1)

while 1:
    clientsock,clientaddr=s.accept()
    print "Got connection from",clientsock.getpeername()
    clientsock.close()
