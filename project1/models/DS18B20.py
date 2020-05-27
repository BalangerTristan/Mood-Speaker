class DS18B20:

    def __init__(self, address):
        self.address = address

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

dd