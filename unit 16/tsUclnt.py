from socket import *

HOST = '119.29.16.209'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

udpCliSocket = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input('>')
    if not data:
        break
    udpCliSocket.sendto(data,ADDR)
    data = udpCliSocket.recvfrom(BUFSIZE)
    if not data:
        break
    print data

udpCliSocket.close()