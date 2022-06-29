from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet import CapuletEngine
from battery.nubbin_battery import NubbinBattery
from engine.sternman import SternmanEngine
from engine.willoughby import WilloughbyEngine
from tire.carrigan import CarriganTire
from tire.octoprime import OctoprimeTire


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTire(tires)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTire(tires)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tires):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTire(tires)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTire(tires)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTire(tires)
        car = Car(engine, battery, tires)
        return car

