from abc import abstractmethod


class Vehicle:
    # Must implement abstract methods
    @abstractmethod # annotation
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass

    ## Might be implemented/overriden if required
    def drive(self):
        print("Vehicle is in motion")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with key ignition")

    def stop_engine(self):
        print("Car engine stopped with key ignition")

class ElectricCar(Vehicle):
    def start_engine(self):
        print("Car engine started silently with button press")

    def stop_engine(self):
        print("Car engine stopped silently with button press")

## Creating Vehicle objects
ferrai = Car()
ferrai.start_engine()
ferrai.drive()
ferrai.stop_engine()

print("\n")
tesla = ElectricCar()
tesla.start_engine()
tesla.drive()
tesla.stop_engine()