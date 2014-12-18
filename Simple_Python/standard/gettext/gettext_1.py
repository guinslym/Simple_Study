# -*- coding:utf-8 -*-
# /usr/bin/env/python

import gettext

#Set up message catalog access
t = gettext.translation('example','locale',fallback=True)
_ = t.ugettext

print _('This message is in the script.')