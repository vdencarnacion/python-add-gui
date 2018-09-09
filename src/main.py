'''
Author: Vivienne Encarnacion
Date: September 9, 2018
'''

import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QLabel

app = QApplication(sys.argv)
# label = QLabel("Hello World!")
label = QLabel("<font color=red size=40>Hello World!</font>")
label.show()
app.exec_()
