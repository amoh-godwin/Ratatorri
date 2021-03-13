import sys

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

from connector import Connector


app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.load('UI/main.qml')
engine.rootObjects()[0].setProperty('connector', Connector())
engine.quit.connect(app.quit)

sys.exit(app.exec())
