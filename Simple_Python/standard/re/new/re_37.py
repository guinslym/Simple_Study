#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import re

address = re.compile(
    r'''
    # The regular name
    (?P<first_name>\w+)      #first name
    \s+
    (([\w.]+)\s+)?  #optional middle name or initial
    (?P<last_name>\w+)     #last name
    \s+
    <

    # The address:first_name.last_name@domain.tld
    (?P<email>
     (?P=first_name)         #first name
    \.
    (?P=last_name)          #last name
    @
    ([\w\d.]+\.)+    #domain name prefix
    (com|org|edu)  #limit the allowed top-level domains
    )
    ''',
    re.UNICODE|re.VERBOSE|re.IGNORECASE)

candidates = [
  u'First Last <first.last@example.com>',
  u'Different Name <first.last@example.com>',
  u'First Middle Last <first.last@example.com>',
  u'First M. Last <first.last@example.com>',
]

for candidate in candidates:
    print 'Candidate:',candidate
    match = address.search(candidate)
    if match:
        print ' Match name :',match.groupdict()['first_name']
        print match.groupdict()['last_name']
        print ' Match email :',match.groupdict()['email']
    else:
        print ' No match'