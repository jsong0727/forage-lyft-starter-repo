from engine.engine import Engine

class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        miles_driven = self.current_mileage - self.last_service_mileage
        if miles_driven > 30000:
            return True
        else:
            return False
