# Created on 13th March, 2021
from threading import Thread

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

import model
import misc

class Connector(QObject):


    """
    This class will serve as a connector
    between the python and the Qml
    """


    def __init__(self):
        QObject.__init__(self)

    usersFetched = pyqtSignal(str, arguments=['_get_users'])

    @pyqtSlot()
    def get_users(self):
        u_thread = Thread(target=self._get_users)
        u_thread.daemon = True
        u_thread.start()

    def _get_users(self):

        users = model.see_all()
        parsed_users = misc.convert_users_to_json(users)
        self.usersFetched.emit(parsed_users)
