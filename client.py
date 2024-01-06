import socket
import os

s = socket.socket()
s.connect(('127.0.0.1', 12345))
print('the client is connected')

def put(file_name):
    global s
    size = os.path.getsize(file_name)
    file_name, file_format = os.path.split(file_name)
    size = str(size)
    s.send(b"put file\n")
    s.send(size.encode('utf-8') + b'\n')
    s.send(file_name.encode('utf-8') + b'\n')
    s.send(file_format.encode('utf-8') + b'\n')
    with open(file_name + file_format, 'rb') as f:
        bytes = f.read()
    s.send(bytes)

def get(filename):
    pass

def disconnect():
    pass

put('received_file.png')