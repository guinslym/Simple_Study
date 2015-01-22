#! /us/bin/env/python
# -*- coding:utf-8 -*-

import fractions

f1 = fractions.Fraction(1,2)
f2 = fractions.Fraction(3,4)

print '%s + %s = %s' % (f1,f2,f1+f2)
print '%s - %s = %s' % (f1,f2,f1-f2)
print '%s * %s = %s' % (f1,f2,f1*f2)
print '%s / %s = %s' % (f1,f2,f1/f2)