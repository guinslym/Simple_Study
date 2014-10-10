#!/usr/bin/env/python
#-*- coding:utf-8 -*-

from __future__ import print_function
from PIL import Image
import os,sys

size=(128,128)
for infile in sys.argv[1:]:
    outfile=os.path.splitext(infile)[0]+'thumb'
    if infile!=outfile:
        try:
            im=Image.open(infile)
            im.thumbnail(size)
            im.save(outfile,'jpeg')
        except IOError:
            print('cannot create thumbnail for',infile)

