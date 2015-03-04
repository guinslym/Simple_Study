#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import pkgutil

template = pkgutil.get_data('pkgwithdata','templates/base.html')
print template.encode('utf-8')