import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
# use the QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import *
# start my_app
my_app = QApplication(sys.argv)
# open webpage
my_web = QWebEngineView()
my_web.load(QUrl("http://free-tutorials.org"))
my_web.show()
# sys exit function
sys.exit(my_app.exec_())
