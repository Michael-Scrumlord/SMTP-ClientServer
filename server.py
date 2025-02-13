# Daylan Stoica - DAYLANSTOICA@csu.fullerton.edu
# Michael Daza - Michael.Daza@csu.fullerton.edu
# Gregory Martinez - greg-2000@csu.fullerton.edu
# Mathew Wheatley - mmwheatley@csu.fullerton.edu


#import socket module 
from socket import * 
import sys # In order to terminate the program 

serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a server socket 

#Fill in start
CONNECTION_DATA = ("127.0.0.1", 8080)
serverSocket.bind(CONNECTION_DATA)

serverSocket.listen()
#Fill in end 

while True: 
    #Establish the connection 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end
    try:
        message = connectionSocket.recv(1024) #Fill in start #Fill in end
        filename = message.split()[1] 
        f = open(filename[1:]) 
        outputdata = f.readlines()
        f.close() #Fill in start #Fill in end
    #Send one HTTP header line into socket 
    #Fill in start
        status = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(status.encode())
    #Fill in end 
    #Send the content of the req uested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError: 
        print("File not found!")
    #Send response message for file not found 
    #Fill in start
        status = "HTTP/1.1 404 Not Found"
        connectionSocket.send(status.encode())
    #Fill in end 
    #Close client socket 
    #Fill in start
    connectionSocket.close()
    #Fill in end 
    sys.exit() #Terminate the program after sending the corresponding data
