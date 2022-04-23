#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import time

HOST = 'ec2-54-227-64-84.compute-1.amazonaws.com'
PORT = 7000
server_addr = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_addr)
f = open("test_data","rb")
data = f.read()

start_time = time.time()
client.send(data)
#resp = client.recv(1024)
#print(resp.decode())
end_time = time.time()
elapsed_time = end_time - start_time
print("TCP socket")
print("elapsed time:"+str(elapsed_time)+" seconds")
f.close()

   

