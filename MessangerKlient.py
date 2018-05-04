#-*- coding: utf-8 -*-

import socket


def client():
    host = "127.0.0.1"
    port = 7677
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    msg = raw_input("\n -> ")
    encoded_msg = bytes(msg)
    while msg != 'q':
        s.send(encoded_msg)
        msg = raw_input("\n -> ")
        encoded_msg = bytes(msg)


client()