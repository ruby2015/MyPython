from socket import *

HOST = '119.29.16.209'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)


while True:
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('>')
    if not data:
        break
    tcpCliSock.send('%s\r\n'% data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print data.strip()
tcpCliSock.close()