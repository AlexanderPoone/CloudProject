#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

HOST = '0.0.0.0'
PORT = 7000
BUFF_SIZE = 65000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    indata, addr = s.recvfrom(BUFF_SIZE)
    print('recvfrom ' + str(addr))

    #outdata = 'received'
    #s.sendto(outdata.encode(), addr)
