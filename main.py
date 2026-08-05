import socket

ip = "127.0.0.1"
port = 80

sock = socket.socket()
sock.connect((ip, port))