from .Mcp import Mcp
from threading import Thread
from repositories.DataRepository import DataRepository
import time
from RPi import GPIO
import subprocess
import os
import signal


class PIR(Thread):

    def __init__(self, socket):
        Thread.__init__(self)
        self.Mcp = self.setup()
        self.socket = socket
        self.playing = False

    def inlezen_PIR(self):
        return round(self.Mcp.read_channel(1)/1023)

    def run(self):
        previous_state = 0
        while True:
            PIR = self.inlezen_PIR()
            DataRepository.meting(3, PIR)
            self.socket.emit('PIR', {'Waarde': PIR})
            current_state =  PIR
            if current_state != previous_state:
                if current_state == 1:
                    if not (self.playing):
                        self.play_streaming_link('Hey')
                        self.playing = True
                    else:
                        self.stop_playing()
                        self.playing = False
                    time.sleep(4)
            previous_state = current_state


    def play_streaming_link(self, link):
        self.process = subprocess.Popen(
            "mpg123 http://icecast.vrtcdn.be/stubru-high.mp3", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

    def stop_playing(self):
        os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        mcp = Mcp(0, 0)
        return mcp
        print('Starting up the PIR Module')
        time.sleep(2)
        print('Ready')
