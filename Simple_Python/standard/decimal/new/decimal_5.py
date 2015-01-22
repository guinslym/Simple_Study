#! /us/bin/env/python
# -*- coding:utf-8 -*-

import decimal
import pprint

context = decimal.getcontext()

print 'Emax  =',context.Emax
print 'Emin   =',context.Emin
print 'capitals =',context.capitals
print 'prec =',context.prec
print 'rounding =',context.rounding
print 'flags ='
pprint.pprint(context.flags)
print 'traps ='
pprint.pprint(context.traps)