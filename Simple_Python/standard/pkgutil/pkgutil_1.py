#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import demopkg
print 'demopkg  :',demopkg.__file__

try:
    import demopkg.shared
except Exception, err:
    print 'demopkg.shared : Not found (%s)' % err
else:
    print 'demopkg.shared :',demopkg.shared.__file__

try:
    import demopkg.not_shared
except Exception, err:
    print 'demopkg.not_shared : Not found (%s)' % err
else:
   print 'demopkg.not_shared :',demopkg.not_shared.__file__