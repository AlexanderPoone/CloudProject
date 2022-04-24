#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

HOST = '0.0.0.0'
PORT = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

conn, addr = s.accept()
RecvData = conn.recv(65000)
while RecvData:
    print('recvfrom ' + str(addr))
    RecvData = conn.recv(65000)
    #conn.send('received'.encode())
conn.close()
