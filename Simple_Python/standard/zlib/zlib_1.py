import zlib

mydata="This is the original text."

fmt="%15s %15s"
print fmt %("len(data}","len(compressed")
print fmt %("-"*15,"-"*15)

for i in xrange(5):
    data = mydata*i
    compressed=zlib.compress(data)
    highlight="*" if len(data)<len(compressed) else ""
    print fmt % (len(data),len(compressed)),highlight
