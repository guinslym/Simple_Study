#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import profile
from profile_2 import fib,fib_seq

if __name__ == '__main__':
    profile.runctx('print fib_seq(n);print',globals(),{'n':20})