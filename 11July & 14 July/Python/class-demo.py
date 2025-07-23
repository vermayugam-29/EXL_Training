class Car :
    def __init__(self, manufracturer, model, year):
        self.manufracturer = manufracturer
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Brand : {self.manufracturer}, Model : {self.model},Year : {self.year}")
