#UTA Id: 1000538439
#Name: Hamilton Nguyen
#References
#1.Skeleton code provided for python as per instructor request.
#2.https://www.youtube.com/watch?v=o_ZpjmZ-uBM&t=1s
#3.https://bedfordsarah.wordpress.com/2013/10/29/python-socket-programming-project-1-http-web-server/
#4.https://www.positronx.io/create-socket-server-with-multiple-clients-in-python/#:~:text=%20Python%20Multithreading%20Example%3A%20Create%20Socket%20Server%20with,in%20Python.%20The%20server%20must%20run...%20More%20
#5.https://docs.python.org/2/library/socket.html
#6.https://docs.python.org/2/howto/sockets.html
#7.http://www.wellho.net/resources/ex.php4?item=y303/browser.py

# Import socket module
import socket

# Import thread module
from _thread import *

import threading 

# Create a TCP server socket
serverSocket = socket.socket()  

# Assign a port number
host = '127.0.0.1'
serverPort = 8080
ThreadCount = 0
hostname = socket.gethostname()

# Bind the socket to server address and server port
try:
    serverSocket.bind((host, serverPort))
except socket.error as e:
    print(str(e))    

# Listen to at most 5 connection at a time

serverSocket.listen(5)

# Server should be up and running and listening to the incoming connections

def multi_thread(connectionSocket):
    try:
        connectionSocket.send(str.encode('Server is working:'))

        # Extract the path of the requested object from the message

        message = connectionSocket.recv(1024).decode('utf-8')

        f = open(message,'rb')

        # Store the entire contenet of the requested file in a temporary buffer

        outputdata = f.read()

        # Send the HTTP response header line to the connection socket
        connectionSocket.send('\nHTTP/1.1 200 OK\n')

        # Send the content of the requested file to the connection socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
        print('Files Received...')

    # Close the socket in case of some issues 
    except:
        connectionSocket.send(b'\nHTTP/1.1 404 Not Found\n')
        connectionSocket.close()
        
while True:
    #This part is for multi threading
    print ('\nReady to serve from server side...')
    Client, address = serverSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    
    #'''Print other client socket values here '''
    print ("Client HOST Name:", hostname)
    print ("Client Socket Name:",Client.getsockname())
    print ("Client Socket Family:",Client.family)
    print ("Client Socket Type:",Client.type)
    print ("Client Protocol:", Client.proto)
    print ("Client Socket get Peer Name:", Client.getpeername())
    print ("Client Timeout:",Client.gettimeout())
    
    #Start the new thread
    start_new_thread(multi_thread, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))    
serverSocket.close()





