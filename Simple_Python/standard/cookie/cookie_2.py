# -*- coding:utf-8 -*-
#! /usr/bin/env/python

import Cookie

c = Cookie.SimpleCookie()
c['mycookie']='cookie_value'
print c