#!/usr/bin/python
#coding: utf-8

import socket

def server():
    proto = socket.getprotobyname('tcp')
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto)

    serv.bind(("localhost", 7677))
    serv.listen(1)
    return serv

serv = server()

while 1:

    conn, addr = serv.accept()
    while 1:
        message = conn.recv(1024)
        print message
        if message:
            conn.send('Hi, I am a server, I received your\'s message: ' + message)
        else: break

    conn.close()