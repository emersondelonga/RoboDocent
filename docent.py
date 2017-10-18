import us
import movement
SAFE_DISTANCE = 15
DEBUG= 1
UR_TRIG_B = 20
UR_ECHO_B = 21
UR_TRIG_T = 5
UR_ECHO_T = 6

topUs = us.__init__(self, UR_TRIG_T, UR_ECHO_T)
bottomUs = us.__init__(self, UR_TRIG_B, UR_ECHO_B)
def main():
    while !KeyboardInterrupt:
        if topUs.too_close(SAFE_DISTANCE) or bottomUs.too_close(SAFE_DISTANCE):
            turn_off_motors()
        else:
            drive_forwards()
        if DEBUG == 1:
            print get_distance()
        
    eyw2.clear_res()
