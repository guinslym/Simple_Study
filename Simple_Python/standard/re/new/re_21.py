#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def test_patterns(text,patterns=[]):
    """Given source text and a list of patterns,look for matches for each pattern within
    the text and print them to stdout."""
    # Look for each pattern in the text and print the results
    for pattern,desc in patterns:
        print 'Pattern %r (%s)\n'% (pattern,desc)
        print '   %r' % text
        for match in re.finditer(pattern,text):
            s = match.start()
            e = match.end()
            prefix = ' '*(s)
            print '  %s%r%s '%(prefix,text[s:e],' '*(len(text)-e)),
            print match.groups()
            if match.groupdict():
                print '%s%s' % (' '*(len(text)-s),match.groupdict())
        print
    return

if __name__ == '__main__':
    test_patterns(
        'abbaabbba',
        [(r'a((a*)(b*))','a followed by 0-n a and 0-n b'),
        ])