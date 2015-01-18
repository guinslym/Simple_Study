#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import re

twitter = re.compile(
    '''
    # A twitter handler:@username
    (?<=@)
    ([\w\d_]+)          #username
    ''',
    re.UNICODE|re.VERBOSE)

text = '''This text includes two Twitter handles.One for @ThePSF,and one for the author,
          @doughellmann.'''

print text
for match in twitter.findall(text):
    print 'Handle:',match