#! /us/bin/env/python
# -*- coding:utf-8 -*-

import fractions
import decimal

for v in [decimal.Decimal('0.1'),
             decimal.Decimal('0.5'),
             decimal.Decimal('1.5'),
             decimal.Decimal('2.0'),
             ]:
    print '%s = %s' % (v,fractions.Fraction.from_decimal(v))