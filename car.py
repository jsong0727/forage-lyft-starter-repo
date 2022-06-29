from battery.battery import Battery
from engine.engine import Engine
from tire.tire import Tire


class Car:
    def __init__(self, engine, battery, tire):
        self.engine = Engine
        self.battery = Battery
        self.tire = Tire

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
