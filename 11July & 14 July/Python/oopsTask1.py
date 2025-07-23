class Vehicle:
    def start(self):
        print("Broom Broom")

class Car(Vehicle):
    def honk(self):
        print("Pee Pee Poo Poo")

obj = Car()

obj.honk()
obj.start()