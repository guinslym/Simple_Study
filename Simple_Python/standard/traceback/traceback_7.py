#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import traceback
import sys
from pprint import pprint
from traceback_1 import call_function

def f():
    return traceback.format_stack()
formatted_stack = call_function(f)
pprint(formatted_stack)