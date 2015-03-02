#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import inspect
import example
from inspect_15 import *

print_class_tree(inspect.getclasstree([example.A,example.B,C,D],
                                                           unique=True,
                                                           ))