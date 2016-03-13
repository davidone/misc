#!/usr/bin/env python

from grovepi import *
from grove_rgb_lcd import *

dht_sensor_port = 7
dht_sensor_type = 0
distance_threshold = 20
ultrasonic_ranger = 4

#setRGB(0,128,64)
#setRGB(0,255,0)

try:
    (temp, hum) = dht(dht_sensor_port, dht_sensor_type)
    distance = ultrasonicRead(ultrasonic_ranger)
    if (distance <= distance_threshold):
        setRGB(0,255,0)
        setText("Temp: {:d}C       Humidity : {:d}%".format(int(temp), int(hum)))
    else:
        setRGB(0,0,0)
        setText("")
    print "{:d}#{:d}".format(int(temp), int(hum))
except (IOError,TypeError) as e:
    print "Error"

exit(0)
