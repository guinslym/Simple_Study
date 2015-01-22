#! /us/bin/env/python
# -*- coding:utf-8 -*-

import math

print '{:^8} {:^8} {:^8}'.format('Degrees','Radians','Expected')
print '{:-^8} {:-^8} {:-^8}'.format('','','')

for rad, expected in [ (0,                  0),
                       (math.pi/6,         30),
                       (math.pi/4,         45),
                       (math.pi/3,         60),
                       (math.pi/2,         90),
                       (math.pi,          180),
                       (3 * math.pi / 2,  270),
                       (2 * math.pi,      360),
                       ]:
    print '{:8.2f}  {:8.2f}  {:8.2f}'.format(rad,
                                             math.degrees(rad),
                                             expected,
                                             )