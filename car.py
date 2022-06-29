
from battery import Battery
from engine import Engine


class Car:
    def __init__(self):
        self.engine = Engine
        self.battery = Battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
