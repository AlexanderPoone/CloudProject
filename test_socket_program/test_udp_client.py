#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import time

HOST = 'ec2-54-227-64-84.compute-1.amazonaws.com'
PORT = 7000
BUFF_SIZE = 65000
server_addr = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

f = open("test_data","rb")
data = f.read(BUFF_SIZE)


data_list = []
data = f.read(BUFF_SIZE)
data_list.append(data)
while (data):
    data_list.append(data)
    data = f.read(BUFF_SIZE)

start_time = time.time()
for x in data_list:
    s.sendto(x,server_addr)
end_time = time.time()
elapsed_time = end_time - start_time
print("UDP socket")
print("elapsed time:"+str(elapsed_time)+" seconds")
f.close()

   

