#! /us/bin/env/python
# -*- coding:utf-8 -*-

import math

print 'Degrees Radians Sine Cosine Tangent'
print ' ------ '*5

fmt = ' '.join(['%7.2f']*5)

for deg in range(0,361,30):
    rad = math.radians(deg)
    if deg in (90,270):
        t = float('inf')
    else:
        t = math.tan(rad)
    print fmt % (deg,rad,math.sin(rad),math.cos(rad),t)