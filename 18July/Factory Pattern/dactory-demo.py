class Vehicle:
    def start_engine(self):
        raise NotImplementedError('Subclasses must implement this method')

class Bike(Vehicle):
    def start_engine(self):
        print('Bike started')

class Car(Vehicle):
    def start_engine(self):
        print('Car started')

class Truck(Vehicle):
    def start_engine(self):
        print('Truck started')

class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == 'bike':
            return Bike()
        elif vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'truck':
            return Truck()
        else:
            raise ValueError('Invalid vehicle type')

if __name__ == '__main__':
    user = input('Enter your choice(Car/Bike/Truck): ')
    vehicle = VehicleFactory.get_vehicle(user.lower())
    vehicle.start_engine()
