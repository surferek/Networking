#!/usr/bin/python
#coding: utf-8

import os
import socket

host="127.0.0.1"
port=7677
s=socket.socket()
s.bind((host, port))
s.listen(13)

def handle_client(s, addr, i):
    while True:
        data=s.recv(1024)
        decoded_data=data.decode("utf-8")
        if not decoded_data:
                print("\nsuccesfull connection with client " + str(i) + " broken\n")
                break
        print("  Klient nr. " + str(i) + " -> " + decoded_data)

def server():
    i=1
    while i<=13:
        c, addr=s.accept()
        child_pid=os.fork()
        if child_pid==0:
                print("\nsuccessfuly connected with client " + str(i) + str(addr) + "\n")
                handle_client(c, addr, i)
                break
        else:
                i+=1

server()