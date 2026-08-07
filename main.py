import socket

ip = "127.0.0.1"
port = 8080

try:
    sock = socket.socket()
    sock.connect((ip, port))
    print(f"Port {port} is OPEN")
except Exception as e:
    print(f"Error occurred: {e}")