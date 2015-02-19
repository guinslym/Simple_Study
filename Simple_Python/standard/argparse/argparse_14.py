#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import argparse

parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add_argument('-a',action='store')
parser.add_argument('--long-b','-b',
                                    action='store',
                                    help='Long and Short togethor')
parser.add_argument('-b',
                                    action='store',
                                    help='Short alone')
print parser.parse_args(['-h'])