#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import zlib

data=open("zlib_1.py","r").read()
cksum=zlib.adler32(data)
#%12d的意思是输出12位的数字，如果不足12位，以空白填充。
print "Adler32:%12d" %cksum
print "       :%12d" % zlib.adler32(data,cksum)

cksum-zlib.crc32(data)
print "Crc-32:%12d" %cksum
print "      :%12d" % zlib.crc32(data,cksum)