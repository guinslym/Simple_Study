#! /usr/bin/env/python
# -*- coding:utf-8 -*-
__author__ = 'tim'
import sys
from PySide.QtCore import QDateTime,QTimer,SIGNAL
from PySide.QtGui import QApplication,QWidget,QLCDNumber


class MyTimer(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('My Digital Clock')
        timer=QTimer(self)
        self.connect(timer,SIGNAL('timeout()'),self.updtTime)
        self.myTimeDisplay=QLCDNumber(self)
        self.myTimeDisplay.setSegmentStyle(QLCDNumber.Filled)
        self.myTimeDisplay.setDigitCount(8)
        self.myTimeDisplay.resize(500,150)
        timer.start(1000)

    def updtTime(self):
        currentTime=QDateTime.currentDateTime().toString("hh:mm:ss")
        self.myTimeDisplay.display(currentTime)

if __name__ == '__main__':
    try:
        app=QApplication(sys.argv)
        myWindow=MyTimer()
        myWindow.show()
        app.exec_()
        sys.exit(0)
    except NameError:
        print "Name Error:",sys.exc_info()[1]
    except SystemError:
        print "Closing Window..."
    except Exception:
        print sys.exc_info()[1]
