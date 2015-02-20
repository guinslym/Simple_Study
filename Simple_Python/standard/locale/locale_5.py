#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import locale
import time

sample_locales = [('USA','en_US.UTF-8'),
                  ('France','fr_FR.UTF-8'),
                  ('Spain','es_ES.UTF-8'),
                  ('Portugal','pt_PT.UTF-8'),
                  ('Poland', 'pl_PL.UTF-8'),
                 ]

for name,loc in sample_locales:
	locale.setlocale(locale.LC_ALL,loc)
	format = locale.nl_langinfo(locale.D_T_FMT)
	print "{0:.20}s： {1}s".format(name,time.strftime(format))