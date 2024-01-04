import socket
import threading as th


def handel_client(c,addr):
    print(f'has connect from {addr}')
    while True:
        order=''
        while True:
            st=c.recv(1)
            if st==b'\n':
                break
            else:
                order += st.decode()
        if order=="put file":
            print("please put a file")
        elif order == "exit":
            break
        elif order == 'get file':
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
        c , addr = s.accept()
        th.Thread(target=handel_client , args=(c,addr)).start()

main()


