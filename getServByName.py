#!/usr/bin/python
#coding: utf-8


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


#List of application protocols
def getServ():
    serviceList = [

        "daytime",

        "ftp",

        "gopher",

        "http",

        "https",

        "mysql",

        "pop3",

        "ssh",

        "snmp",

        "smtp"]

    underlyingProtocol = "tcp"

    print("======>Services and their port numbers<======")

    for service in serviceList:
        # get the port number for each application protocol which uses TCP as underlying

        portNum = socket.getservbyname(service, underlyingProtocol)

        print("The service {} uses port number {} ".format(service,portNum))


def calculateTime():
    start_time = time.time()
    msg=("--- %s sekund ---" % (time.time() - start_time))
    return msg



def generator():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        port = int(7677)
    except ValueError:
        port = socket.getservbyname(7677, 'tcp')
    s.connect(("127.0.0.1", port))
    s.settimeout(5)
    cnt=0
    while True:
        try:
            cnt += 1                 # Second variant
            print(cnt)               # Second variant
            getServ()                # Second variant
            #print 'Send a sequence to server:', seq(20)   # First variant
            print calculateTime()
            time.sleep(2)
        except KeyboardInterrupt:
            sys.exit(1)
        except:
            continue






if __name__ == '__main__':
    generator()