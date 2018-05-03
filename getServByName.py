import socket
import time
import sys
import random


def seq(length):
    nucl=["A","C","T","G"]
    sequence=[]
    for i in xrange(length):
        tmp=random.choice(nucl)
        sequence.append(tmp)
    return "".join(sequence)


def calculateTime():
    start_time = time.time()
    msg=("--- %s sekund ---" % (time.time() - start_time))
    return msg

def generator():
    count = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        port = int(7677)
    except ValueError:
        port = socket.getservbyname(7677, 'tcp')
    s.connect(("127.0.0.1", port))
    s.settimeout(5)
    while True:
        try:
            s.sendall(b'#Hi')
            print 'Send a sequence to server:', seq(20)
            print calculateTime()
            time.sleep(2)
        except KeyboardInterrupt:
            sys.exit(1)
        except:
            continue


if __name__ == '__main__':
    generator()