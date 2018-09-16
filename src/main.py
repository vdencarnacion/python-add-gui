'''
Author: Vivienne Encarnacion
Date: September 9, 2018
'''

import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QGuiApplication, QWindow	
from PySide2.QtWidgets import QLabel


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    window = QWindow()
    window.setTitle('Hello world!')
    window.show()
    sys.exit(app.exec_())
