#coding:utf-8
import socket,sys

host=sys.argv[1]
textport=sys.argv[2]
filename=sys.argv[3]

try:
    print "Creating socket....",
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error, e:
    print "Strange error creating sock:%s" % e
    sys.exit(1)
print "done"

try:
    port=int(textport)
except ValueError:
    try:
        print "Looking up port number...",
        port =socket.getservbyname("http","tcp")
    except socket.error,e:
        print "Couldn't find your port:%s" %e
        sys.exit(1)
        print "done"
    try:
        print "Connecting to remote host on port %d" % port,
        s.connect(("www.baidu.com",port))
    except socket.gaierror,e:
        print "Address-related error connect to server:%s" %e
        sys.exit(1)
    print "done"

print "Connected from",s.getsockname()
print "Connected to",s.getpeername()
