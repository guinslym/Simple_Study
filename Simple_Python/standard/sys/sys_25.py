#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sys
import textwrap

names = sorted(sys.builtin_module_names)
name_text = ', '.join(names)

print textwrap.fill(name_text,width=65)