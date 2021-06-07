# MultiThreadedWebServer

# References

#1.https://www.youtube.com/watch?v=o_ZpjmZ-uBM&t=1s

#2.https://bedfordsarah.wordpress.com/2013/10/29/python-socket-programming-project-1-http-web-server/

#3.https://www.positronx.io/create-socket-server-with-multiple-clients-in-python/#:~:text=%20Python%20Multithreading%20Example%3A%20Create%20Socket%20Server%20with,in%20Python.%20The%20server%20must%20run...%20More%20

#4.https://docs.python.org/2/library/socket.html

#5.https://docs.python.org/2/howto/sockets.html

#6.http://www.wellho.net/resources/ex.php4?item=y303/browser.py

# Purpose:
The purpose of this document is to comprehensively describe the development of a multi-threaded server and a single
threaded client in python language. This project serves the purpose of understanding network foundation
and concepts related to multi-threading and server-client socket handling.

# Source files:
1.client.py

2.server.py

3.index.html

4.dog.jpeg

# Compilation/Execution Procedures:
##make sure to run the code on Windows 10 operating system##
##make sure to install python current on system##
##make sure to install visual studio code with required python interpretor##

# Server-side:

1. click on server.py file and have it executed automatically in command prompt. 
Alternate: navigate through source folder in CLI using command prompt and type python server.py

2. await and standby the command prompt for the server side. 

# Client-side: 

1. Open browser(any web browser)
2. For HTTP validation: type https://127.0.0.1:8080/index.html
3. Review incoming connection and handling on the server side. Note: Windows 10 security prevent
unauthorized ssl connection(ERR_SSL_PROTOCOL_ERROR), make sure to turn off all security 
countermeasure and open port 80 and 443 in order to execute the hmtl file. Note the exception 
handling on the server side when a 404 error has occurred. Look for this error on server:
(ConnectionAbortedError: [WinError 10053] An established connection was aborted by the 
software in your host machine)
4.For Client connection: Open visual studio code for client.py
5. Run python file in the terminal by clicking on the compile button.
Alternate: navigate through source folder in CLI using visual studio code and type python client.py
6. observe the client-server handling on both sides of the command prompt terminal. All data information
shall be included as per requirement of the assignment.
