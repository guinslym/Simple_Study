# -*- coding:utf-8 -*-
# /usr/bin/env/python

import locale

sample_locales = [('USA','en_US.UTF-8'),
                             ('France','fr_FR.UTF-8'),
                             ('Spain','es_ES.UTF-8'),
                             ('Portugal','pt_PT.UTF-8'),
                             ('Poland', 'pl_PL.UTF-8'),
                            ]

for name,loc in sample_locales:
	locale.setlocale(locale.LC_ALL,loc)
	print '%20s: %10s %10s' %(name,
                                                     locale.currency(1234.56),
                                                     locale.currency(-1234.56))