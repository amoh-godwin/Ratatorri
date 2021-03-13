# Created on 13th March, 2021

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class Connector(QObject):


    """
    This class will serve as a connector
    between the python and the Qml
    """


    def __init__(self):
        QObject.__init__(self)
