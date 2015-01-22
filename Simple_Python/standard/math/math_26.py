#! /us/bin/env/python
# -*- coding:utf-8 -*-

import math

print '{:^7} {:^7} {:^10}'.format('X','Y','Hypotenuse')
print '{:-^7} {:-^7} {:-^10}'.format('','','')

for x,y in [ # simple points
    (1,1),
    (-1,-1),
    (math.sqrt(2),math.sqrt(2)),
    (3,4), #3-4-5 triangle
    # on the circle
    (math.sqrt(2)/2,math.sqrt(2)/2), #pi/3 rads
    (0.5,math.sqrt(3)/2) #pi/3 rads
]:
    h = math.hypot(x,y)
    print '{:7.2f} {:7.2f} {:7.2f}'.format(x,y,h)