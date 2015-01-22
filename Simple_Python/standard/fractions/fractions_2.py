#! /us/bin/env/python
# -*- coding:utf-8 -*-

import fractions

for s in ['1/2','2/4','3/6']:
    f = fractions.Fraction(s)
    print '%s = %s' % (s,f)