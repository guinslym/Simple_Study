# -*- coding: utf-8 -*-
#!/usr/bin/env python2
"""
常见加密函数,可以实现crc32,md5,sha128,sha256,sha512加密
"""
from __future__ import print_function
import sys
import hashlib
import zlib
import base64

def Crypt(algo,data):
    algo = str.lower(algo)
    if algo in hashlib.algorithms:
        crypt_type = hashlib.new(algo)
        for compute in chunk_size(64,data):
            crypt_type.update(data)
        return crypt_type.hexdigest()
    elif algo in ['crc32','adler32']:
        result = getattr(zlib,algo)(data)&0xffffffff
        return result
    elif algo in ['b64encode','b32encode','b16encode','b64decode','b32decode','b16decode']:
        return getattr(base64,algo)(data)

def chunk_size(str_len,data):
    data_len = len(data)
    data_start = 0
    while data_start < data_len:
        compute = data[data_start:data_start+str_len]
        yield compute
        data_start +=str_len
    return

if __name__ == '__main__':
    algo = sys.argv[1]
    content = sys.argv[2]
    print(Crypt(algo,content))