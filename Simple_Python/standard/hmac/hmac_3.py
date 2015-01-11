#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import hmac
import hashlib
import base64

with open('untitled','rb') as f:
    body = f.read()

hash = hmac.new('secret-shared-key-goes-here',body,hashlib.sha1)
digest = hash.digest()
print base64.encodestring(digest)