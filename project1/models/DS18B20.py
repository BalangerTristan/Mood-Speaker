from threading import Thread
import time
from repositories.DataRepository import DataRepository

class DS18B20(Thread):

    def __init__(self, address, socket):
        Thread.__init__(self)
        self.address = address
        self.socket = socket

    @property
    def address(self):
        """The address property."""
        return self._address

    @address.setter
    def address(self, value):
        if type(value) == str:
            self._address = value
        else:
            raise ValueError("Address type isn't valid")

    @property
    def __one_wire_file(self):
        """The __one_wire_file property."""
        return f'/sys/devices/w1_bus_master1/{self.address}/w1_slave'

    def inlezen_temp(self):
        data = open(self.__one_wire_file)
        temperatuur = data.read().split('t=')[1][:-1]
        data.close()
        return float(f'{temperatuur[:-3]}.{temperatuur[-3:]}')

    def run(self):
        while True:
            temperatuur = self.inlezen_temp()
            DataRepository.meting(1, temperatuur)
            self.socket.emit('temperatuur', {'Waarde': temperatuur})
            time.sleep(25)
