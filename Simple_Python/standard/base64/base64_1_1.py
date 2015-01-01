import base64
encode=base64.b64encode("data to be encoded")
data=base64.b64decode(encode)
print "enocde:"
print encode
print "decode:"
print data
f1=file("base.txt","r")
f2=file("base64.txt","w")
base64.encode(f1,f2)
f1.close()
f2.close()
