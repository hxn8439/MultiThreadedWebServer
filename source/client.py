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

# import libraries
import socket
from time import *
import sys
import time
import datetime

#Values are setted as per assignment requirements. HN 3-11-2021
HOST = '127.0.0.1'
PORT = 8080
#Requested_file_name
fileName = 'dog.jpeg'
hostname = socket.gethostname()

#handle client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Client has been established')

#server_add() function was not implemented since it serves no purpose as a client code. Hn 3-11-2021
#server_add = ()

#connect the host and port to the socket
clientSocket.connect((HOST, PORT))
send_time = time.time()
clientSocket.send(b'fileName')

data=clientSocket.recv(1024)
recv_time = time.time()
RTT = recv_time - send_time
print('Data received by the client is', data)
print('RTT ', RTT)

#'''Print other server socket values here '''
print ("Server HOST Name:", hostname)
print ("Server Socket Name:",clientSocket.getsockname())
print ("Server Socket Family:",clientSocket.family)
print ("Server Socket Type:",clientSocket.type)
print ("Server Protocol:", clientSocket.proto)
print ("Server Socket get Peer Name:", clientSocket.getpeername())
print ("Server Timeout:",clientSocket.gettimeout())

#terminate and close socket
clientSocket.close()