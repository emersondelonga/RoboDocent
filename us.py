

import pigpio, eyw2
import numpy as np
trig = 20
echo = 21
class US:
    """ A class for an ultrasonic sensor."""
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        self.readings = [128, 128, 128, 128, 128]

    def get_distance(self): 

        currentReading =  eyw2.read_ultrasonic_ranger(trig, echo)
        if currentReading != none:
            readings.pop(0)
            readings.append(currentReading)

        return np.mean(readings)
    def too_close(dist): 
        if currentReading <= dist:
            return true
        else:
            return false
