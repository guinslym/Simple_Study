import socket

for host in ["homer","www"]:
    print "%6s:%s"%(host,socket.getfqdn(host))
    
