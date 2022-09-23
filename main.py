class Phones:
    buttons = 0
    dynamic = 0
    microphones = 0
    battery = 0

    def __init__(self, buttons, dynamic, microphones, battery):
        self.buttons = buttons
        self.dynamic = dynamic
        self.microphones = microphones
        self.battery = battery

    def iphone(self, buttons):
        self.buttons = buttons

    def samsung(self, dynamic, microphones):
        self.dynamic = dynamic
        self.microphones = microphones

    @classmethod
    def charge_phone(cls):
        return Phones(1, 2, 3, 4)

    @classmethod
    def discharge(cls):
        cls.battery -= 1
        return Phones(5, 6, 7, 8)

    @classmethod
    def fabrika_phones(cls):
        cls.battery += 1
        return Phones(9, 10, 11, 12)

    @staticmethod
    def processor():
        print("Processor is the phone brain")

    @staticmethod
    def connect_antena():
        print("Connecting people")

device = Phones(1, 2, 3, 4)

Phones.iphone(device, 5)
device.iphone(3)
device.samsung(7, 6)
Phones.charge_phone()
Phones.discharge()
Phones.fabrika_phones()
Phones.processor()
Phones.connect_antena()