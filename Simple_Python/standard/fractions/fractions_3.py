#! /us/bin/env/python
# -*- coding:utf-8 -*-

import fractions

for s in ['0.5','1.5','2.0']:
    f = fractions.Fraction(s)
    print '%s = %s' % (s,f)