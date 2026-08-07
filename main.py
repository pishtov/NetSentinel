import socket

ip = "127.0.0.1"
port = 80

try:
    sock = socket.socket()
    sock.connect((ip, port))
except Exception as e:
    print(f"Error occurred: {e}")