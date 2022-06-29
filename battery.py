from datetime import datetime


class Battery:
    def __init__(self):
        self.current_date = datetime.today().date()
        self.last_service_date = None

    def battery_life(self, year):
        self.year = year

    def needs_service(self):
        years_serviced = self.last_service_date - self.current_date
        if years_serviced > self.year:
            return True
        else:
            return False
