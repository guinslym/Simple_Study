__author__ = 'tim'

from PyQt5.QtWidgets import QApplication,QCalendarWidget
import sys

app=QApplication(sys.argv)
cal=QCalendarWidget()
cal.show()
sys.exit(app.exec_())
