#!/usr/bin/env/python
#-*- coding:utf-8 -*-
__author__ = 'tim'

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QGridLayout


class GridLayOut(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self)

        self.setWindowTitle('Grid Layout')
        title=QLabel('Title')
        author=QLabel('Author')
        review=QLabel('Review')

        titleEdit=QLineEdit()
        authorEdit=QLineEdit()
        reviewEdit=QLineEdit()

        grid=QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit,3, 1, 5, 1)

        self.setLayout(grid)
        self.resize(350,400)

app=QApplication(sys.argv)
qb=GridLayOut()
qb.show()
sys.exit(app.exec_())
