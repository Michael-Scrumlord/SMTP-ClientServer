# Daylan Stoica - DAYLANSTOICA@csu.fullerton.edu
# Michael Daza - Michael.Daza@csu.fullerton.edu
# Gregory Martinez - greg-2000@csu.fullerton.edu
# Mathew Wheatley - mmwheatley@csu.fullerton.edu

from socket import *
import sys

serverIP = str(sys.argv[1])
serverPort = int(sys.argv[2])
fileName = str(sys.argv[3])

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))

request = 'GET /{c} HTTP/1.1\r\nHost: {a}:{b}'.format(a = serverIP, b = serverPort, c = fileName)
clientSocket.send(request.encode())

responseHeader = clientSocket.recv(1024).decode('utf-8')
print('Response Header from Server: ', responseHeader)

response_body = clientSocket.recv(1024)
print('\n Response Body from the Server: ', response_body.decode())

input = input("\nPress any key to close.")

clientSocket.close
