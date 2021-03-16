# Created on 13th March, 2021
from threading import Thread
from time import sleep

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

    usersFetched = pyqtSignal(list, arguments=['_get_users'])
    nroll_name = pyqtSignal(list, arguments=['nroll_cou'])

    @pyqtSlot()
    def get_users(self):
        u_thread = Thread(target=self._get_users)
        u_thread.daemon = True
        u_thread.start()

    def _get_users(self):
        sleep(0.5)
        users = model.see_all()
        parsed_users = misc.convert_users_to_json(users)
        self.usersFetched.emit(parsed_users)

    @pyqtSlot()
    def start_nroll_cou(self):
        u_thread = Thread(target=self._start_nroll_cou)
        u_thread.daemon = True
        u_thread.start()

    def _start_nroll_cou(self):
        sleep(0.5)
        pass

