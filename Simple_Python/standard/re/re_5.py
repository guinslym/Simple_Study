#coding:utf-8
import re
import codecs
import sys

sys.stdout=codecs.getwriter("UTF-8")(sys.stdout)
text="Francais say 中国是个很好的旅游地方".decode("utf-8")
pattern=ur"\w+"
ascii_pattern=re.compile(pattern)
unicode_pattern=re.compile(pattern,re.UNICODE)

print "Text       :",text
print "Pattern    :",pattern
print "ASCII      :",u",".join(ascii_pattern.findall(text))
print "Unicode    :",u",".join(unicode_pattern.findall(text))