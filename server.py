import socket
import os
import ssl
from datetime import datetime
import pytz

def IND():
    now = datetime.now()
    data = now.strftime("%H:%M:%S")
    return data
    
def USA():
    tz = pytz.timezone('America/New_York')
    now = datetime.now(tz)
    data = now.strftime("%H:%M:%S")
    return data

def UK():
    tz = pytz.timezone('Europe/London')
    now = datetime.now(tz)
    data = now.strftime("%H:%M:%S")
    return data

def AUS():
    tz = pytz.timezone('Australia/Sydney')
    now = datetime.now(tz)
    data = now.strftime("%H:%M:%S")
    return data

def JPN():
    tz = pytz.timezone('Asia/Tokyo')
    now = datetime.now(tz)
    data = now.strftime("%H:%M:%S")
    return data

def RSA():
    tz = pytz.timezone('Africa/Maputo')
    now = datetime.now(tz)
    data = now.strftime("%H:%M:%S")
    return data

def SA():
    tz = pytz.timezone('Chile/Continental')
    now = datetime.now(tz)
    data = now.strftime("%H:%M:%S")
    return data

HOST = '127.0.0.1'
PORT = 2121
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

password = input("Enter SSL certificate password: ")
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.check_hostname = False
ssl_context.load_cert_chain(certfile="server.cer", keyfile="server.key", password=password)
ssl_sock = ssl_context.wrap_socket(serverSocket, server_side=True)

ssl_sock.bind((HOST,PORT))
ssl_sock.listen()
conn,addr = ssl_sock.accept()
print(f'connected with:{HOST,PORT} ')

while True:
    print('waiting to receive data...')
    Data = conn.recv(1024).decode()
    print(f'\nrecieved data: {Data}\n')

    if Data =='IND':
       conn.sendall(IND().encode()) 
    elif Data =='USA':
       conn.sendall(USA().encode()) 
    elif Data =='UK':
       conn.sendall(UK().encode()) 
    elif Data =='AUS':
       conn.sendall(AUS().encode()) 
    elif Data =='JPN':
       conn.sendall(JPN().encode()) 
    elif Data =='RSA':
       conn.sendall(RSA().encode()) 
    elif Data =='SA':
       conn.sendall(SA().encode()) 
    elif Data =='quit' or Data=='QUIT':
        break
    else:
        message = 'timezone not found'
        conn.sendall(message.encode())