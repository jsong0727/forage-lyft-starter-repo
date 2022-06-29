from abc import abstractmethod
from battery import Battery
from engine import Engine


class Car:
    def __init__(self):
        self.engine = Engine
        self.battery = Battery

    @abstractmethod
    def needs_service(self):
        pass
