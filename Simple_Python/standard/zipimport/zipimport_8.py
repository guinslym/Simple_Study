#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os
import example
print example.__file__
data_filename = os.path.join(os.path.dirname(example.__file__),
                                             '__init__.py')
print data_filename,':'
print open(data_filename,'rt').read()