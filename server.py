import socket
import threading as th

def handel_client(c, addr):
    print(f'has connect from {addr}')
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
            bytes=b''
            while True:
                st=c.recv(1)
                if not st:
                    break
                bytes += st

            with open(name.decode()+'recv'+format.decode(),'wb') as f:
                f.write(bytes)


        elif order == b"exit":
            break
        elif order == b'get file':
            pass
        else:
            pass

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
