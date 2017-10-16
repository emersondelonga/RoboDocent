#avg over small time

import pigpio, eyw2
import numpy as np

class US:
    """ A class for an ultrasonic sensor."""
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        self.readings = [128, 128, 128, 128, 128]

    def get_distance():

        currentReading =  eyw2.read_ultrasonic_ranger(trig, echo)
        if currentReading != null:
            readings.pop(0)
            readings.append(currentReading)

        return np.mean(readings)
