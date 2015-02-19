#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import getopt

opts,args = getopt.getopt(['-a','-bval','-c','val'],'ab:c:')
for opt in opts:
    print opt