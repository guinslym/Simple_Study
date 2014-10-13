#! /usr/bin/env/python
# -*- coding:utf-8 -*-
__author__ = 'tim'

import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication,QLabel

if __name__ == '__main__':
    app=QApplication(sys.argv)

    label=QLabel()
    label.setText("hello world")
    label.setAlignment(Qt.AlignCenter)
    label.setWindowTitle('My First Application')
    label.setGeometry(300,300,350,100)

    label.show()

    sys.exit(app.exec_())
