from .Mcp import Mcp
from threading import Thread
from repositories.DataRepository import DataRepository
import time
from RPi import GPIO

class LDR(Thread):

    def __init__(self, socket):
        Thread.__init__(self)
        self.Mcp = self.setup()
        self.socket = socket

    def inlezen_licht(self):
        return self.to_percentage(self.Mcp.read_channel(0))
        

    def run(self):
        while True:
            licht = self.inlezen_licht()
            DataRepository.meting(2, licht)
            self.socket.emit('Licht', {'Waarde': licht})
            time.sleep(10)

    def to_percentage(self, value):
        return round(100-(value/(1000.0-21.0)*100.0), 2)

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        mcp = Mcp(0, 0)
        return mcp

