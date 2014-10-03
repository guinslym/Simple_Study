import socket
from time import ctime

HOST=""
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
	print "Waiting for connecting..."
	tcpSerSock,addr=tcpSerSock.accept()
	print "...connected from:",addr

	while True:
		data=tcpSerSock.recv(BUFSIZ)
		if not data:
			break
		tcpSerSock.send("[%s]%s"%(ctime(),data))

	tcpSerSock.close()
tcpSerSock.close()