#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from urlparse import urldefrag

original = 'http://netloc/path;param?query=arg#frag'
print 'original:',original
url,fragment = urldefrag(original)
print 'url   :',url
print 'fragment:',fragment