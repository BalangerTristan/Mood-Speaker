import spidev


class Mcp:
    def __init__(self, bus=0, device=0):
        self.bus = bus
        self.device = device
        self._spi = spidev.SpiDev(self.bus, self.device)
        self._spi.max_speed_hz = 10 ** 5

    @property
    def bus(self):
        return self._bus

    @bus.setter
    def bus(self, value):
        self._bus = value

    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, value):
        self._device = value

    def read_channel(self, channel=0):
        bytes_in = self._spi.xfer2([1, (8+channel) << 4, 0])
        return bytes_in[1] << 8 | bytes_in[2]

    def closespi(self):
        self._spi.close()
        del(self)

# def to_percentage(value):
#     return round(100-(value/(1000.0-21.0)*100.0), 2)

# def setup():
#     GPIO.setmode(GPIO.BCM)
#     global mcp
#     mcp = Mcp(0, 0)


# try:
#     setup()
#     while True:
#         print(to_percentage(mcp.read_channel(0)), "%")
# except KeyboardInterrupt as e:
#     print(e)
# finally:
#     mcp.closespi()
#     print('Script ended!')
#     GPIO.cleanup()

