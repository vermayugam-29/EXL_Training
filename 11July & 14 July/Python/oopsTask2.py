class Chef :
    def cook(self):
        print("Cooking food")

class Driver:
    def drive(self):
        print("Driving vehicle")

class Person(Driver,Chef):
    def work(self):
        print("Working multitask")

person = Person()
person.work()
person.cook()
person.drive()