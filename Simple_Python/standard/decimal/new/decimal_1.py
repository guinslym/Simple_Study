#! /us/bin/env/python
# -*- coding:utf-8 -*-

import decimal

fmt = '{0:<25}{1:<25}'
print fmt.format('Input','Output')

# Integer
print fmt.format(5,decimal.Decimal(5))

# String
print fmt.format('3.14',decimal.Decimal('3.14'))

# Float
f = 0.1
print fmt.format(repr(f),decimal.Decimal(str(f)))
print fmt.format('%.23g'%f,str(decimal.Decimal.from_float(f))[:25])