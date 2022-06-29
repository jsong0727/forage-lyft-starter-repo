from battery import Battery
from car import Car
from engine import Engine

#Engine
capulet = Engine()
capulet.max_mileage(30000)
willoughby = Engine()
willoughby.max_mileage(60000)
sternman = Engine()


#Batteries
spindler = Battery()
spindler.battery_life(2)
nubbin = Battery()
nubbin.battery_life(4)

#Car
calliope = Car()
calliope.engine = capulet
calliope.battery = spindler

glissade = Car()
glissade.engine = willoughby
glissade.battery = spindler

palindrome = Car()
palindrome.engine = sternman
palindrome.battery = spindler

rorschach = Car()
rorschach.engine = willoughby
rorschach.battery = nubbin

thovex = Car()
thovex.engine = capulet
thovex.battery = nubbin
