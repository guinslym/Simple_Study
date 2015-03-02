#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import inspect
import example
import pprint

pprint.pprint(inspect.getsourcelines(example.A.get_name))