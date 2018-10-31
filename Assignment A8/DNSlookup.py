import socket

import os

while True:

    try:
        choice=input('Enter Choice: \n1. Name to address\n2. Address to Name\n3. nsLookup\n')

        if choice=='1':
            print('Address is : ', socket.gethostbyname(input('\nEnter name of host : ')))
        elif choice=='2':
            print('Name is : ', socket.gethostbyaddr(input('Enter address of host : ')))  # type >>>import socket >>>help(socket.gethostbyaddr) 
        elif choice=='3':
            os.system('nslookup '+ input('Enter host name or address : '))
        else:
            break

    except Exception as e:
        print('Exception occured\n', e)