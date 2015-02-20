# -*- coding:utf-8 -*-
# /usr/bin/env/python

import locale

sample_locales = [('USA','en_US.UTF-8'),
                  ('France','fr_FR.UTF-8'),
                  ('Spain','es_ES.UTF-8'),
                  ('Portugal','pt_PT.UTF-8'),
                  ('Poland', 'pl_PL.UTF-8'),
                 ]

print '{0:.20}s {1:.15}s {2:.20}s'.format('Locale','Integer','Float')
for name,loc in sample_locales:
	locale.setlocale(locale.LC_ALL,loc)

	print '%20s' % name,
	print locale.format('%15d',123456,grouping=True)
	print locale.format('%20.2f',123456.78,grouping=True)