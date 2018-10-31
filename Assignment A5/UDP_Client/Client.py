import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 5000)

filename = input('Enter file name you wish to recieve from the server: ')
sock.sendto(bytes(filename, encoding='UTF-8'), server_address)
with open(filename, 'wb') as file:
    data, _ = sock.recvfrom(65535)
    file.write(data)
sock.close()