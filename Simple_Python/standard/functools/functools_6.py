#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import functools

class MyObject(object):
    def __init__(self,val):
        self.val = val
    def __str__(self):
        return 'MyObject (%s)' %self.val

def compare_obj(a,b):
    """Old-style comparison function."""
    print 'comparing %s and %s' %(a,b)
    return cmp(a.val,b.val)

# Make a key function using cmp_to_key()
get_key = functools.cmp_to_key(compare_obj)

def get_key_wrapper(o):
    """Wrapper function for get_key to allow for print statements."""
    new_key = get_key(o)
    print 'key_wrapper (%s) -> %s' %(o,new_key)
    return new_key

objs = [MyObject(x) for x in xrange(5,0,-1)]

for o in sorted(objs,key=get_key_wrapper):
    print o