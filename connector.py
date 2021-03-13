# Created on 13th March, 2021
from threading import Thread

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal


class Connector(QObject):


    """
    This class will serve as a connector
    between the python and the Qml
    """


    def __init__(self):
        QObject.__init__(self)

    @pyqtSlot()
    def get_users(self):
        u_thread = Thread(target=self._get_users)
        u_thread.daemon = True
        u_thread.start()

    def _get_users(self):
        print('yam')
