from abc import ABC
import exceptions

class Vehicle(ABC):
    def __init__(self,started, weight=100, fuel=10, fuel_consumption=1):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if self.started is not True:
            print('Начинаем движение!')
            if self.fuel > 0:
                self.started = True
                print('Готов к движению!')
            else:
                raise exceptions.LowFuelError('В баке нет топлива.')

    def move(self, dist_km):
        fuel_to_move = dist_km * self.fuel_consumption
        if self.fuel >= fuel_to_move:
            self.fuel = self.fuel - fuel_to_move
            return f'В баке осталось {self.fuel} топлива'
        else:
            raise exceptions.NotEnoughFuel('Мало топлива')