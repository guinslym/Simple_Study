# /usr/bin/env python
# -*- coding:utf-8 -*-

import time


def fact(n):
    s=time.time()
    result=0
    if n==0 or n==1:
        return n
    else:
        result=n*(fact(n-1))
        e=time.time()
        print (e-s)
        return result

fact(999)

