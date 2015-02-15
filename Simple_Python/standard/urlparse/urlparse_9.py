#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from urlparse import urljoin

print urljoin('http://www.example.com/path/','subpath/file.html')
print urljoin('http://www.example.com/','subpath/anotherfile.html')