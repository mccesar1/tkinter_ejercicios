import binascii
from http import client
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.0.238', 7086)

print('starting up on {} port {}'.format(*server_address))
sock.connect(server_address)

#leer 
Read = bytes([0x55, 0x0a, 0x0d, 0x04, 0x91, 0x01, 0x01, 0x00, 0x81, 0x61])
#dejar de leer
StopRead = bytes([0x55, 0x0b, 0x0d, 0x03, 0x20, 0x00, 0x01, 0x74, 0xd4])

def IniciarLectura():
    sock.send(Read)

def DetenerLectura():
    
    sock.send(StopRead)

#sock.send(Read)

#IniciarLectura()
DetenerLectura()
#sock.send(StopRead)

#sock.send((Read))
#client.write(new Uint8Array([0x55, 0x0a, 0x0d, 0x04, 0x91, 0x01, 0x01, 0x00, 0x81, 0x61]));
# Listen for incoming connections
#sock.listen(1)

while True:
    #print (sys.stderr, '\nwaiting to receive message') 

    data = sock.recv(4096)   
    #data = sock.listen(1) 
    #print (data)
    
    #data2 = sock.recvfrom(4096)  
    #print (sys.stderr, 'received %s bytes from %s' % (len(data))) 
    #print (sys.stderr, data) 
    if data:
        #thetime = time.strftime("%Y-%m-%d %a %H:%M:%S", time.localtime()) 
        if len(data) > 0:
         data = str(binascii.hexlify(data))
         #550a0109910001900000010002a705
         
         data = data[16:28]
         #data = data[1:40] 
         print ("Card Scanned. Tag ID:", data)    # print the tag number
         #print ("card = ", [data])

# while True:
#     # Wait for a connection
#     print('waiting for a connection')
#     #connection, client_address = sock.accept()
#     try:
#         print('connection from', client_address)

#         # Receive the data in small chunks and retransmit it
#         while True:
#             data = connection.recv(16)
#             print('received {!r}'.format(data))
#             if data:
#                 print('sending data back to the client')
#                 connection.sendall(data)
#             else:
#                 print('no data from', client_address)
#                 break

#     finally:
#         # Clean up the connection
#         connection.close()