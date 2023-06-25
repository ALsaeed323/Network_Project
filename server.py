import threading
print("Threading module imported successfully")

from socket import *
print("Socket module imported successfully")

def handle_client(connectionSocket):
    print("Handling client...")
    try:
        message = connectionSocket.recv(1024)
        print(f"Received message from client: {message}")
        
        filename = message.split()[1]
        print(f"Filename extracted from message: {filename}")#/test.html
        
        f = open(filename[1:])
        print(f"File opened successfully: {filename[1:]}")#test.html
        
        outputdata = f.read()
        print(f"File read successfully: {filename[1:]}")
        
        connectionSocket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        print("HTTP response header sent to client")

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        print(f"Data sent to client: {outputdata}")
        
        connectionSocket.close()
        print("Connection closed with client")
    except IOError:
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
        print("File not found. 404 error sent to client")
        connectionSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)
print("Server socket created")

serverPort = 80
print("Server port defined as: ", serverPort)

serverSocket.bind(("127.0.0.1", serverPort))
print("Server socket bound to port")

# Start listening for incoming connections, allowing a backlog of 5 connections
serverSocket.listen(5)
print("Server started listening for incoming connections")

# Loop indefinitely to keep accepting new connections
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print(f"Accepted connection from {addr}")
    
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))
    print("New client thread created")

    client_thread.start()
    print("Client thread started")
    serverSocket.close()
    print("Server socket closed")


