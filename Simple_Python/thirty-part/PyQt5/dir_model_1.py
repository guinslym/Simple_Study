#!/usr/bin/env/python
#-*- coding:utf-8 -*-
__author__ = 'tim'

import sys
from PyQt5.QtWidgets import QApplication, QTableView,QWidget,QDirModel,QGridLayout,QListView,QTreeView
from PyQt5.QtCore import QDir


class Dir_Model(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)

        self.setWindowTitle('View')
        dirModel=QDirModel()
        lay=QGridLayout(self)
        lv=QListView()
        lay.addWidget(lv,0,0)
        lv.setModel(dirModel)

        lvi=QListView()
        lay.addWidget(lvi,0,1)
        lvi.setViewMode(QListView.IconMode)
        lvi.setModel(dirModel)

        trv=QTreeView()
        lay.addWidget(trv,1,0)
        trv.setModel(dirModel)

        tav=QTableView()
        tav.setModel(dirModel)
        lay.addWidget(tav,1,1)

        cwdIndex=dirModel.index(QDir.currentPath())
        lv.setRootIndex(cwdIndex)
        lvi.setRootIndex(cwdIndex)
        trv.setRootIndex(cwdIndex)
        tav.setRootIndex(cwdIndex)


app=QApplication(sys.argv)
d=Dir_Model()
d.show()
sys.exit(app.exec_())