import threading
import time

import RPi.GPIO as GPIO

from Act.control_motor import move, remote_car_irw
from Sensory.control_IR_sensor import sensor
from Sensory.control_camera import camera
from Sensory.control_irw import init_irw, next_key
from Sensory.control_sonar import measure


def main_v0():
    while True:
        if measure() < 20 or sensor() < 2:
            # avoid obstacles
            move("down", t=0.2)
            move("left", t=0.2)
        else:
            move("up", t=0.2)

def main_v1():
    init_irw()
    previous_key = None
    previous_time = None

    while True:
        keyname, updown  = next_key()
        current_time = time.time()
        if keyname == previous_key and (current_time - previous_time) < 1.5:
            tmp = keyname
            keyname = None
            remote_car_irw(tmp)
        previous_time = current_time
        previous_key = keyname
        

def main_v2():
    init_irw()
    while True:
        keyname, updown = next_key()
        remote_car_irw(keyname)


if __name__ == '__main__':
    try:
        t = threading.Thread(target=main_v1, args=())
        t.daemon = True
        t.start()
        print "car ready to go"
        
        camera()
        print "camera ready"
    except KeyboardInterrupt:
        GPIO.cleanup()
