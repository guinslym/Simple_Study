#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import urllib

query_args = {'q':'query string','foo':'bar'}
encoded_args = urllib.urlencode(query_args)
print 'Encoded:',encoded_args

url = 'http://localhost:80/test.php?'+encoded_args
print urllib.urlopen(url).read()