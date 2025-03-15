from abc import abstractmethod

class Aircraft():
    # Must implement abstract methods
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

    # Might be implemented/overridden if required
    def fly(self):
        print("Aircraft is in flight")

class Airplane(Aircraft):
    def start_engine(self):
        print("Airplane engine started with turbo engines")

    def stop_engine(self):
        print("Airplane engine stopped")

class PrivateJet(Aircraft):
    def start_engine(self):
        print("Private jet engine started with jet thrust")

    def stop_engine(self):
        print("Private jet engine stopped")

## Creating Aircraft objects
boeing_747 = Airplane()
boeing_747.start_engine()
boeing_747.fly()
boeing_747.stop_engine()

print("\n")
gulfstream = PrivateJet()
gulfstream.start_engine()
gulfstream.fly()
gulfstream.stop_engine()