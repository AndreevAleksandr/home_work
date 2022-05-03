import  Vehicle
import Engine

class Car(Vehicle.Vehicle):
    def __init__(self):
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine