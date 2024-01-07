import os.path
import socket
import threading as th

def handel_client(c, addr):
    print(f'has connect from {addr}')
    try:
        while True:
            order = b''
            while True:
                st = c.recv(1)
                if not st:
                    break
                if st == b'\n':
                    break
                else:
                    order += st

            if order == b"put file":
                size = b''
                name = b''
                format = b''
                while True:
                    st = c.recv(1)
                    if st == b'\n':
                        break
                    else:
                        size += st

                print(f'The size is {size.decode("utf-8")}')
                while True:
                    st = c.recv(1)
                    if st == b'\n':
                        break
                    else:
                        name += st

                while True:
                    st = c.recv(1)
                    if st == b'\n':
                        break
                    else:
                        format += st

                print('start to rev bytes')
                bytes = b''
                while True:
                    st = c.recv(int(size.decode()))
                    if not st:
                        break
                    else:
                        bytes += st

                with open(name.decode() + 'recv' + format.decode(), 'wb') as f:
                    f.write(bytes)
                print('revc file complated')

            elif order == b"exit":
                break

            elif order == b'get file':
                print('starting to send file')
                name = b''
                format = b''
                while True:
                    st = c.recv(1)
                    if st == b'\n':
                        break
                    elif not st:
                        break
                    else:
                        name += st

                while True:
                    st = c.recv(1)
                    if st == b'\n':
                        break
                    elif not st:
                        break
                    else:
                        format += st

                size = os.path.getsize(name.decode() + format.decode())
                size = str(size)
                c.send(size.encode() + b'\n')
                with open(name.decode() + 'recv' + format.decode(), 'rb') as f:
                    bytes = f.read()
                c.send(bytes)
                print(f"{name.decode() + 'recv' + format.decode()} was send")
    except:
        try:
            c.close()
        except:
            pass
    print(f'{addr} disconnected')


def main():
    s = socket.socket()
    port = 12345
    print(f'The port is {port}')
    s.bind(('', port))
    s.listen(10)
    print('The server is listning')
    while True:
        c, addr = s.accept()
        th.Thread(target=handel_client, args=(c, addr)).start()

main()
