#! /usr/bin/env/python
# -*- coding:utf-8 -*

import base64

encodes_with_pluses = chr(251) + chr(239)
encodes_with_slashes = chr(255)*2

for original in [encodes_with_pluses,encodes_with_slashes]:
    print 'Original',repr(original)
    print 'Standard encoding:',base64.standard_b64encode(original)
    print 'URL-safe encoding:',base64.urlsafe_b64encode(original)