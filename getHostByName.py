#!/usr/bin/python



import socket, sys,time

def getHostIP(domain_name):
    ip_addr = socket.gethostbyname(domain_name)
    start_time = time.time()
    msg = ("%s sekund" % (time.time() - start_time))
    return ip_addr,msg

if __name__ == '__main__':
    domain = sys.argv[1]
    print "Adres IP dla domeny %s to %s czas wyszukania wynosi %s" % (domain, getHostIP(domain)[0],getHostIP(domain)[1])
