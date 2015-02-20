#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import locale

sample_locales = [('USA','en_US.UTF-8','1,234.56'),
                  ('France','fr_FR.UTF-8','1234,56'),
                  ('Spain','es_ES.UTF-8','1234,56'),
                  ('Portugal','pt_PT.UTF-8','1234.56'),
                  ('Poland', 'pl_PL.UTF-8','1234,56'),
                 ]

for name,loc,a in sample_locales:
	locale.setlocale(locale.LC_ALL,loc)
	f = locale.atof(a)
	print "{0:.20}s： {1:.9}s => {2}f".format(name,a,f)