import hashlib

data="This is the example about hashlib"
h=hashlib.sha1()
h.update(data)
print h.hexdigest()

