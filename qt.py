#! /usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
     
    window = QWidget()
    button = QPushButton('button', window)
    window.show()
 
    sys.exit(app.exec_())
