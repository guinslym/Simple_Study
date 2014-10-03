import hashlib

data="This is the example about hashlib"
h=hashlib.md5()
h.update(data)
print h.hexdigest()

