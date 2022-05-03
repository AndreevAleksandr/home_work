import  Vehicle
import exceptions

class Plane(Vehicle.Vehicle):
    def __init__(self, max_cargo, cargo = 0):
        super().__init__(self, max_cargo, cargo)
        self.max_cargo = max_cargo
        self.cargo = cargo

    def load_cargo(self, num):
        cargo_total = self.cargo + num
        if self.max_cargo >= cargo_total:
            self.cargo = cargo_total
            print(f'Общий груз: {cargo_total}')
        else:
            raise exceptions.CargoOverload('Машина перегружена!!!')

    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before