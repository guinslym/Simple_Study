#! /us/bin/env/python
# -*- coding:utf-8 -*-

import math

print '{:^4} {:^4} {:^5} {:^5}'.format('x','y','%','fmod')
print '----'*4

for x,y in [(5,2),
               (5,-2),
               (-5,2),
            ]:
    print '{:4.1f} {:4.1f} {:5.2f} {:5.2f}'.format(
        x,
        y,
        x % y,
        math.fmod(x,y),
        )