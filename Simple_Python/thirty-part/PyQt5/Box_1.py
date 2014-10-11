#!/usr/bin/env/python
#-*- coding:utf-8 -*-
__author__ = 'tim'

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout


class BoxLayOut(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self)

        self.setWindowTitle('Box Layout')
        ok=QPushButton('OK')
        cancel=QPushButton('Cancel')
        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(ok)
        hbox.addWidget(cancel)

        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.resize(300,150)


app=QApplication(sys.argv)
bl=BoxLayOut()
bl.show()
sys.exit(app.exec_())
