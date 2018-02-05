import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
left_in = 32
right_in = 36

GPIO.setup(left_in, GPIO.IN)
GPIO.setup(right_in, GPIO.IN)

def sensor():
    sensor_l = GPIO.input(left_in)
    sensor_r = GPIO.input(right_in)
    sensor_ = int(sensor_l) + int(sensor_r)
    return sensor_

if __name__ == "__main__":
    while 1:
        sensor_ = sensor()
        if sensor_ == 0:
            print("left & right")
        elif sensor_ == 1:
            print("l || r")
        elif sensor_ == 2:
            print("nothing")
