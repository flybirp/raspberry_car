import socket
import time 

SOCKPATH = "/var/run/lirc/lircd"
sock = None

def init_irw():
    global sock
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    print('starting up on %s' % SOCKPATH)
    sock.connect(SOCKPATH)

def next_key():
    while True:
        data = sock.recv(128)
        data = data.strip()
        words = data.split()
        if len(words) == 4:
            break
    return words[2], words[1]


def ir_receive():
    previous_key = None
    previous_time = None
    while True:
        keyname, updown = next_key()
        current_time = time.time()
        if keyname == previous_key and (current_time - previous_time) < 1.5:
            tmp = keyname
            keyname = None
            print tmp, updown
        previous_time = current_time
        previous_key = keyname

def ir_recei():
    while True:
        keyname, updown = next_key()
        print('%s %s' % (keyname, updown))


if __name__ == '__main__':
    init_irw()
    ir_receive()
