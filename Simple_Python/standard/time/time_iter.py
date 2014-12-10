# /usr/bin/env python
# -*- coding:utf-8 -*-

import time


def fact(n):
    if n==0:
        return n
    s=time.time()
    i=0
    prod=1
    while i<n:
        i += 1
        prod = prod*i

    e=time.time()
    print (e-s)
    return prod

fact(1000)