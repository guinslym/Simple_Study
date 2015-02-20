#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import shlex

for s in ['Do "Not" Separate',
             '"Do"Separate',
             'Escaped \e Character not in quotes',
             'Escaped "\e" Character in double quotes',
             "Escaped '\e' Character in single quotes",
             r"Escaped '\'' \"\'\" Single quote",
             "\"'Strip extra layer of quotes'\"",
             ]:
    print 'ORIGINAL:',repr(s)
    print 'non-POSIX:',
    non_posix_lexer = shlex.shlex(s,posix=False)
    try:
        print repr(list(non_posix_lexer))
    except ValueError,err:
        print 'error(%s)' % err

    print 'POSIX  :'
    posix_lexer = shlex.shlex(s,posix=True)
    try:
        print repr(list(posix_lexer))
    except ValueError,err:
        print 'error(%s)' % err
    print