#!/usr/bin/env/python
#-*- coding:utf-8 -*-
__author__ = 'tim'

import sys
from PyQt5.QtWidgets import QApplication, QLabel

app=QApplication(sys.argv)
label=QLabel('Hello World')
label.setWindowTitle('Hello')
label.setGeometry(200,200,200,40)
label.show()
sys.exit(app.exec_())

