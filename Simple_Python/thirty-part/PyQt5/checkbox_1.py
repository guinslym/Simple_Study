__author__ = 'tim'

import sys
from PyQt5.QtWidgets import QCheckBox,QApplication
app=QApplication(sys.argv)
checkbox=QCheckBox('male')
checkbox.show()
sys.exit(app.exec_())