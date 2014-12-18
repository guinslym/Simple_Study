# -*- coding:utf-8 -*-
# /usr/bin/env/python

import locale
import time

sample_locales = [('USA','en_US'),
                  ('France','fr_FR'),
                  ('Spain','es_ES'),
                  ('Portugal','pt_PT'),
                  ('Poland', 'pl_PL'),
                 ]

for name,loc in sample_locales:
	locale.setlocale(locale.LC_ALL,loc)
	format = locale.nl_langinfo(locale.D_T_FMT)
	print "{0:.20}s： {1}s".format(name,time.strftime(format))