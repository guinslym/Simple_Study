#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from difflib import SequenceMatcher

def show_results(s):
    i,j,k = s.find_longest_match(0,5,0,9)
    print '  i = %d'%i
    print '  j = %d'%j
    print '  k= %d'%k
    print ' A[i:i+k]=%r' % A[i:i+k]
    print ' B[j:j+k]=%r' % B[j:j+k]

A = ' abcd'
B = 'abcd abcd'

print 'A = %r' % A
print 'B = %r' % B

print '\nWithout junk detection:'
show_results(SequenceMatcher(None,A,B))

print '\nTreat spaces as junk:'
show_results(SequenceMatcher(lambda x:x==" ",A,B))