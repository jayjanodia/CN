import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 5000)
sock.bind(server_address)

filename, clientaddress =sock.recvfrom(65535)
with open(filename.decode(encoding='UTF-8'), 'rb') as file:
    sock.sendto(file.read(65535),clientaddress)
    print('Completed successfully, copied file ', print(filename.decode(encoding='UTF-8')))
sock.close()