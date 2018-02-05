import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)



def buzz():
    p = GPIO.PWM(8, 6888)
    p.start(0)

    for i in range(0, 1):
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.04)
        #for dc in range(100, -1, -5):
        #    p.ChangeDutyCycle(dc)
        #    time.sleeap(0.1)
    p.stop()

if __name__ == "__main__":
    buzz()
