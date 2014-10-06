__author__ = 'tim'

import sys
from PyQt5.QtWidgets import QApplication,QPushButton
app=QApplication(sys.argv)
button=QPushButton('hello world')
button.show()
sys.exit(app.exec_())
