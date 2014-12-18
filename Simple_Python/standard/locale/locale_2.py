# -*- coding:utf-8 -*-
# /usr/bin/env/python

import locale

sample_locales = [('USA','en_US'),
                  ('France','fr_FR'),
                  ('Spain','es_ES'),
                  ('Portugal','pt_PT'),
                  ('Poland', 'pl_PL'),
                 ]

for name,loc in sample_locales:
	locale.setlocale(locale.LC_ALL,loc)
	print '%20s: %10s %10s' %(name,locale.currency(1234.56),locale.currency(-1234.56))