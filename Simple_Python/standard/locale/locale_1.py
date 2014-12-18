# -*- coding:utf-8 -*-
# /usr/bin/env/python

import locale
import os
import pprint
import codecs
import sys

sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)

#Default settings based on the user's environment
locale.setlocale(locale.LC_ALL,'')

print 'Environment settings:'
for env_name in ['LC_ALL','LC_CTYPE','LANG','LANGUAGE']:
	print '\t%s = %s' % (env_name,os.environ.get(env_name,''))

#What is the locale?
print
print 'Locale from environment:',locale.getlocale()

template = """
Numeric formatting:
  Decimal point     :"%(decimal_point)s"
  Grouping positions:%(grouping)s
  Thousands separator:"%(Thousands_sep)s"

Monetary formatting:
  International currency symbol       :"%(int_curr_symbol)r"
  Local currency symbol               :%(currency_symbol)r
  Unicode version                     :%(currency_symbol_u)s
  Symbol precedes positive value      :%(p_cs_precedes)s
  Symbol precedes negative value      :%(n_cs_precedes)s
  Decimal point                       :%(mon_decimal_point)s
  Digits in fractional values         :%(frac_digits)s
  Digits in fractional values,international:%(int_frac_digits)s
  Grouping positions                  :%(mon_grouping)s
  Thousands separator                 :"%(mon_thousands_seq)s"
  Positive sign                       :"%(positions_sign)s"
  