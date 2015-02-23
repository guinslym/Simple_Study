#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import profile

def fib(n):
    # from literateprograms.org
    # http://bit.ly/h10Q5m
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fib_seq(n):
    seq = []
    if n >0:
        seq.extend(fib_seq(n-1))
    seq.append(fib(n))
    return seq

profile.run('print fib_seq(20);print')