import socket
import sys


def http_client(server_host, server_port, filename):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((server_host, server_port))

    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
    clientSocket.send(request.encode())

    response = b""
    while True:
        recv_data = clientSocket.recv(1024)
        if not recv_data:
            break
        response += recv_data

    print(response.decode())
    clientSocket.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: client.py server_host server_port filename")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    http_client(server_host, server_port, filename)
