# -*- coding:utf-8 -*-
# /usr/bin/env/python

import locale

sample_locales = [('USA','en_US','1,234.56'),
                  ('France','fr_FR','1234,56'),
                  ('Spain','es_ES','1234,56'),
                  ('Portugal','pt_PT','1234.56'),
                  ('Poland', 'pl_PL','1 234,56'),
                 ]

for name,loc,a in sample_locales:
	locale.setlocale(locale.LC_ALL,loc)
	f = locale.atof(a)
	print "{0:.20}s： {1:.9}s => {2}f".format(name,a,f)