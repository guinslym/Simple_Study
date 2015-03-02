#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import inspect
import example
from pprint import pprint

pprint(inspect.getmembers(example.A),width=65)