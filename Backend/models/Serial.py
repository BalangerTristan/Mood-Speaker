import time
import serial
from threading import Thread
from repositories.DataRepository import DataRepository


class Serial(Thread):

    # INIT / START
    def __init__(self, socket, par_port, par_baudrate=9600, par_parity=serial.PARITY_NONE, par_stopbits=serial.STOPBITS_ONE, par_bytesize=serial.EIGHTBITS, par_timeout=1):
        Thread.__init__(self)
        self.socket = socket
        self.__port = par_port
        self.__baudrate = par_baudrate
        self.__parity = par_parity
        self.__stopbits = par_stopbits
        self.__bytesize = par_bytesize
        self.__timeout = par_timeout

        self.arduino = serial.Serial(str(self.__port), baudrate=self.__baudrate, parity=self.__parity,
                                     stopbits=self.__stopbits, bytesize=self.__bytesize, timeout=self.__timeout)

    # Functies

    def write(self, par_input):
        self.arduino.write(bytes(par_input, "utf-8"))
        time.sleep(1)

    def read(self):
        read = self.arduino.readline()

    def close_port(self):
        self.arduino.close()

    def run(self):

        while True:
            Temp = DataRepository.get_latest_value(1).get('Waarde')
            LDR = DataRepository.get_latest_value(2).get('Waarde')
            if LDR < 25:
                if Temp < 18:
                    self.write('PATTERN')
                    self.read()
                    self.write('DarkBlue')
                    self.read()
                elif Temp >= 18 and Temp < 21:
                    self.write('PATTERN')
                    self.read()
                    self.write('Blue')
                    self.read()
                elif Temp >= 21 and Temp < 24:
                    self.write('PATTERN')
                    self.read()
                    self.write('Red')
                    self.read()
                elif Temp >= 24:
                    self.write('PATTERN')
                    self.read()
                    self.write('DarkRed')
                    self.read()
