#! /us/bin/env/python
# -*- coding:utf-8 -*-

import math

print '{:^7} {:^7} {:^7}'.format('Degrees','Radians','Expected')
print '{:-^7} {:-^7} {:-^7}'.format('','','')

for deg,expected in [
    (0,0),
    (30,math.pi/6),
    (45,math.pi/4),
    (90,math.pi/2),
    (180,math.pi),
    (270,3/2.0*math.pi),
    (360,2*math.pi)
    ]:
    print '{:7d} {:7.2f} {:7.2f}'.format(deg,
                                                   math.radians(deg),
                                                   expected,
                                                   )