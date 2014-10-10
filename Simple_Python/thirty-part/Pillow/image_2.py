#!/usr/bin/env/python
#-*- coding:utf-8 -*-
__author__ = 'tim'

from PIL import Image

im=Image.open('1.jpg')
im=im.rotate(180)
im.save('2.jpg')
