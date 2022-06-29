from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tires):
        self.tires = tires

    def needs_service(self):
        if sum(self.tires) >= 3:
            return True
        else:
            return False
