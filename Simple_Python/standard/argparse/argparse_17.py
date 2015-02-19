#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import argparse
import argparse_16

parser = argparse.ArgumentParser(
    parents=[argparse_16.parser],
    )
parser.add_argument('--local-arg',
                                   action='store_true',
                                   default=False)
print parser.parse_args()