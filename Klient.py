#!/usr/bin/python
#
# KLIENT
#
import socket

import time

def loop():
    while True:
        print "DoS"
        time.sleep(1)


def sendPacket():
    proto = socket.getprotobyname('tcp')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto)
    try:
        s.connect(("127.0.0.1", 7677))
        start_time = time.time()
        msg=("--- %s sekund ---" % (time.time() - start_time))
        s.send(msg)

        resp = s.recv(1024)
        print resp
    except socket.error:
        pass
    finally:
        s.close()

if __name__ == '__main__':
    sendPacket()