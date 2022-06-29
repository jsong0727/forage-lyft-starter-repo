

class Engine:
    def __init__(self):
        self.current_mileage = None
        self.last_service_mileage = None
        self.warning_light_on = False

    def max_mileage(self, mileage):
        self.mileage = mileage

    def needs_service(self):
        miles_driven = self.current_mileage - self.last_service_mileage
        if miles_driven > self.mileage or self.warning_light_on:
            return True
        else:
            return False
