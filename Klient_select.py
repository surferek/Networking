#!/usr/bin/python
#coding: utf-8


import socket

messages = [ 'Hello hello ',
             'there\'s a message',
             'send to you in parts',
             ]
server_address = ('localhost', 7677)

socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM),
          socket.socket(socket.AF_INET, socket.SOCK_STREAM),
          socket.socket(socket.AF_INET, socket.SOCK_STREAM),
          ]

print  'connecting to %s port %s' % server_address
for s in socks:
    s.connect(server_address)

for message in messages:

    for s in socks:
        print  '%s: sending "%s"' % (s.getsockname(), message)
        s.send(message)

    for s in socks:
        data = s.recv(1024)
        print '%s: received "%s"' % (s.getsockname(), data)
        if not data:
            print 'closing socket', s.getsockname()
            s.close()