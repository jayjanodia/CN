import socket
import math

def fileTransfer(sock):
    filename = sock.recv(256).decode(encoding='UTF-8')
    with open(filename, 'rb') as file:
        sock.send(file.read(65535))

def calculator(sock):
    choice=sock.recv(256).decode(encoding='UTF-8')
    num1 = float(sock.recv(8).decode(encoding='UTF-8'))
    num2 = float(sock.recv(8).decode(encoding='UTF-8'))
    if choice == '1':
        sock.send(bytes(str(num1+num2), encoding='UTF-8'))
    elif choice == '2':
        sock.send(bytes(str(num1-num2), encoding='UTF-8'))
    elif choice == '3':
        sock.send(bytes(str(num1*num2), encoding='UTF-8'))
    elif choice == '4':
        sock.send(bytes(str(num1/num2), encoding='UTF-8'))

def trignometry(sock):
    choice=sock.recv(256).decode(encoding='UTF-8')
    angle=float(sock.recv(8).decode(encoding='UTF-8'))
    angle=math.radians(angle)
    if choice == '1':
        sock.send(bytes(str(math.sin(angle)), encoding='UTF-8'))
    elif choice == '2':
        sock.send(bytes(str(math.cos(angle)), encoding='UTF-8'))
    elif choice == '3':
        sock.send(bytes(str(math.tan(angle)), encoding='UTF-8'))

if __name__ == '__main__':

    serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSock.bind(('127.0.0.1',5000))
    serverSock.listen(1)
    sock, addr = serverSock.accept()

    choice = sock.recv(1).decode(encoding='UTF-8')
    if choice == '1':
        sock.send(bytes(sock.recv(65535).decode(encoding='UTF-8').upper(), encoding='UTF-8'))
    elif choice == '2':
        fileTransfer(sock)
    elif choice == '3':
        calculator(sock)
    elif choice == '4':
        trignometry(sock)
    '''else:
        break'''

    sock.close()