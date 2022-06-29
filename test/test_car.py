import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet import CapuletEngine
from engine.sternman import SternmanEngine
from engine.willoughby import WilloughbyEngine


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = date.fromisoformat("2022-06-28")
        last_service_date = date.fromisoformat("2005-06-28")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = date.fromisoformat("2022-06-28")
        last_service_date = date.fromisoformat("2021-06-28")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


# test batteries
class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = date.fromisoformat("2022-06-28")
        last_service_date = date.fromisoformat("2005-06-28")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = date.fromisoformat("2022-06-28")
        last_service_date = date.fromisoformat("2021-06-28")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


# test engines
class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 10000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 10000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine = SternmanEngine(warning_light_on=True)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_on=False)
        self.assertFalse(engine.needs_service())
