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

def get(file_n):
    global s
    file_n, file_f = os.path.split(file_n)
    print(file_n,file_f)
    s.send(b'get file'+b'\n')
    s.send(file_n.encode('utf-8') + b'\n')
    s.send(file_f.encode('utf-8') + b'\n')
    size=b''
    bytes=b''
    while True:
        st=s.recv(1)
        if st==b'\n':
            break
        elif not st:
            break
        size += st

    while True:
        st=s.recv(int(size.decode()))
        if not st:
            break
        bytes += st
    with open(file_n+'send'+file_f,'wb') as f:
        f.write(bytes)

def disconnect():
    global s
    s.send(b'exit'+b'\n')
    s.close()





