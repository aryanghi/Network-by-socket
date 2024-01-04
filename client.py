import socket
import os

s=socket.socket()
s.connect(('127.0.0.1',12345))
print('the clinet is connected')

def put(file_name):
    global s
    s.send("put file".encode() + b'\n')

def get(filename):
    pass

def disconnect():
    pass

