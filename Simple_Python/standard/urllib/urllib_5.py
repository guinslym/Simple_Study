#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import urllib

print urllib.unquote('http%3A//localhost%3A8080/%7Edhellmann/')
print urllib.unquote_plus('http%3A%2Flocalhost%3A8080%2F%7Edhellmann%2F')