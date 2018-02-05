import RPi.GPIO as GPIO
import time
from control_buzzer import buzz


t1 = 12
t2 = 16
t3 = 18
t4 = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(t1, GPIO.OUT)
GPIO.setup(t2, GPIO.OUT)
GPIO.setup(t3, GPIO.OUT)
GPIO.setup(t4, GPIO.OUT)

def makeTurn(name, t):
    if name == "right_backward":
        w = t1
    elif name == "right_forward":
        w = t2
    elif name == "left_backward":
        w = t3
    elif name == "left_forward":
        w = t4
    print name
    GPIO.output(w, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(w, GPIO.LOW)

def forward(t):
    print "forward"
    GPIO.output(t2, GPIO.HIGH)
    GPIO.output(t4, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(t2, GPIO.LOW)
    GPIO.output(t4, GPIO.LOW)

def backward(t):
    print "backward"
    GPIO.output(t1, GPIO.HIGH)
    GPIO.output(t3, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(t1, GPIO.LOW)
    GPIO.output(t3, GPIO.LOW)

def move(name, t):
    if name == "up":
        forward(t)
    if name == "down":
        backward(t)
    if name == "right":
        makeTurn("right_forward", t)
    if name == "left":
        makeTurn("left_forward", t)

def remote_car_irw(tmp):
    if tmp == 'KEY_2':
        move("up", t=0.5)
    if tmp == 'KEY_8':
        move("down", t=0.5)
    if tmp == 'KEY_4':
        move('left', t=0.2)
    if tmp == 'KEY_6':
        move('right', t=0.2)
    if tmp == 'KEY_0':
        buzz()
        print "reward"
