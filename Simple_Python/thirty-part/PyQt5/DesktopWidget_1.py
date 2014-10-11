#!/usr/bin/env/python
#-*- coding:utf-8 -*-
__author__ = 'tim'

import sys
from PyQt5.QtWidgets import QApplication, QWidget,QDesktopWidget


class Center(QWidget):                                                                         #窗口居中显示
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle('Center')
        self.resize(250,150)
        screen = QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)



app=QApplication(sys.argv)
qb=Center()
qb.show()
sys.exit(app.exec_())