#! /us/bin/env/python
# -*- coding:utf-8 -*-

import binascii

def to_hex(t,nbytes):
    """Format text t as a sequence of ntype long values \
    separated by spaces.
    """
    char_per_item = nbytes * 2
    hex_version = binascii.hexlify(t)
    return ' '.join(
        hex_version[start:start+char_per_item]
        for start in xrange(0,len(hex_version),char_per_item)
        )

if __name__ == '__main__':
    print to_hex('abcdef',1)
    print to_hex('abcdef',2)