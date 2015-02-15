#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from urlparse import urljoin

print urljoin('http://www.example.com/path/file.html','anotherfile.html')
print urljoin('http://www.example.com/path/file.html','../anotherfile.html')