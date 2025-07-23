class Device():
    def powerOn(self):
        print("Power on")

class Laptop(Device):
    def code(self):
        print("Coding on Laptop")

class Smartphone(Device):
    def call(self):
        print("Making a call")

lappy = Laptop()
lappy.powerOn()
lappy.code()

mobo = Smartphone()
mobo.powerOn()
mobo.call()