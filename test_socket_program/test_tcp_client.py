#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import time

HOST = 'ec2-34-203-214-59.compute-1.amazonaws.com'
PORT = 7000
server_addr = (HOST, PORT)
BUFF_SIZE = 65000

f = open("test_data_10k","rb")
start_time = time.time()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_addr)
while True:
    data = f.read(BUFF_SIZE)
    if not data:
        break
    ret = client.sendall(data)
    #print(ret)
#resp = client.recv(1024)
#print(resp.decode())
end_time = time.time()
elapsed_time = end_time - start_time
print("TCP socket")
print("elapsed time:"+str(elapsed_time)+" seconds")
f.close()

   

