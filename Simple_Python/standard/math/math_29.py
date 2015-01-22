#! /us/bin/env/python
# -*- coding:utf-8 -*-

import math

print '{:^6} {:^6} {:^6} {:^6}'.format(
    'X','sinh','cosh','tanh',
    )
print '{:-^6} {:-^6} {:-^6} {:-^6}'.format('','','','')

fmt = ' '.join(['{:6.4f}']*4)

for i in range(0,11,2):
    x = i/10.0
    print fmt.format(x,math.sinh(x),math.cosh(x),math.tanh(x))