#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import argparse
import argparse_11

parser = argparse.ArgumentParser(
    parents=[argparse_11.parser],
    )
parser.add_argument('--local-arg',
                                   action='store_true',
                                   default=False)
print parser.parse_args()