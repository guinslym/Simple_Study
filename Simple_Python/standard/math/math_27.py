#! /us/bin/env/python
# -*- coding:utf-8 -*-

import math

print '{:^8} {:^8} {:^8} {:^8} {:^8}'.format(
    'X1','Y1','X2','Y2','Distance',
    )
print '{:-^8} {:-^8} {:-^8} {:-^8} {:-^8}'.format('','','','','')

for (x1,y1),(x2,y2) in [
    ((5,5),(6,6)),
    ((-6,-6),(-5,-5)),
    ((0,0),(3,4)), # 3-4-5 triangle
    ((-1,-1),(2,3)), #3-4-5 triangle
    ]:
    x = x1 - x2
    y = y1 - y2
    h = math.hypot(x,y)
    print '{:8.2f} {:8.2f} {:8.2f} {:8.2f} {:8.2f}'.format(x1,y1,x2,y2,h)