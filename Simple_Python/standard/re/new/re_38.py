#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import re

address = re.compile(
    r'''
    # A name is made up of letters,and may include "."
    # for title abbreviations and middle initials.
    (?P<name>
        ([\w.]+\s+)*[\w.]+
        )?
    \s*
    #Email addresses are wrapped in angle brackets,but only if a name is found
    (?(name)
        # remainer wrapped in angle brackets because there is a name
        (?P<brackets>(?=(<.*>$)))
    |
    # remainder does not include angle brackets without name
    (?=([^<].*[^>]$))
    )

    #Only look for a bracket if the look-ahead assertion found both of them
    (?(brackets)<|\s*)

    #The address itself:usename@domain.tld
    (?P<email>
        [\w\d.+-]+    #usename
    @
    ([\w\d.]+\.)+    #domain name prefix
    (com|org|edu)  #limit the allowed top-level domains
    )
    ''',
    re.UNICODE|re.VERBOSE)

candidates = [
  u'First Last <first.last@example.com>',
  u'No Brackets first.last@example.com>',
  u'Open Bracket <first.last@example.com',
  u'Close Bracket first.last@example.com>',
  u'no.brackets@example.com',
]

for candidate in candidates:
    print 'Candidate:',candidate
    match = address.search(candidate)
    if match:
        print ' Match name :',match.groupdict()['name']
        print ' Match email :',match.groupdict()['email']
    else:
        print ' No match'