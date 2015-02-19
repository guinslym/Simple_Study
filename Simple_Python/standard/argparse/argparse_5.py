#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import argparse

parse = argparse.ArgumentParser(
    description='Change the option prefix characters',
    prefix_chars='-+/',
    )
parse.add_argument('-a',action='store_false',
                                default=None,
                                help='Turn A off',
                                )
parse.add_argument('+a',action='store_true',
                                default=None,
                                help='Turn A on',
                                )
parse.add_argument('//noarg','++noarg',
                                action='store_true',
                                default=False)
print parse.parse_args()