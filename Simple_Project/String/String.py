# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 05:14:02 2015

@author: tim
"""
import string

class String(object):
    def ROT13(self,s):
        """ROT13字符串转换"""
        r = ''.join(map(chr,(range(65,91)+range(97,123))))
        t = ''.join(map(chr,(range(65+13,91)+range(65,65+13)+range(97+13,123)+range(97,97+13))))
        trans=string.maketrans(r,t)
        return s.translate(trans)
    def one_time_pad(self,o,c):
        """一次一密密码
        例如:print one_time_pad('ONETIMEPAD','TBFRGFARFM')
        """
        if(len(o)!=len(c)):
            return
        ascii_list = map(ord,o)
        cipher_list = map(ord,c)
        cipher_text = []
        for i,x in enumerate(ascii_list):
            c_num = x-64+cipher_list[i]
            if c_num>90:
                cipher_text.append(c_num-26)
            else:
                cipher_text.append(c_num)
        return ''.join(map(chr,c_num))
    def one_time_decrypt(c,p):
        """一次一密密码"""
        if len(c)!=len(p):
            return
        cipher_list = map(ord,c)
        cipher_text = map(ord,p)
        origin_list = []
        for i,x in enumerate(cipher_list):
            origin_num = x-cipher_text[i]+64
            if origin_num < 65:
                origin_list.append(origin_num+26)
            else:
                origin_list.append(origin_num)
        return ''.join(map(chr,origin_list))
    def SimpleEncrypt(self,plain,key=7,symbol=3):
        """使用GCD编码字符"""
        plain_text = {
          1: string.ascii_letters,
          2: string.ascii_lowercase,
          3: string.ascii_uppercase
        }
        index = 0
        cipher_text = ''
        for i,s in enumerate(plain_text[symbol]):
            index = (i*key)%len(plain_text[symbol])
            cipher_text += plain_text[symbol][index]
        trans = string.maketrans(plain_text[symbol],cipher_text)
        return plain.translate(trans)

s = String()
#print s.ROT13('Zhangsan')
#print s.ROT13('PHP@124')
#print s.ROT13('Munatfna');
print s.SimpleEncrypt('hElLoWOrLd',7,2)
print s.SimpleEncrypt('hElLoWOrLd',7,3)
print s.SimpleEncrypt('hElLoWOrLd',7,1)