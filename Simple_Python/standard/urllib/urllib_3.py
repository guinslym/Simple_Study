#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import urllib

query_args = {'foo':['foo1','foo2']}
print 'Single      :',urllib.urlencode(query_args)
print 'Sequence:',urllib.urlencode(query_args,doseq=True)