import socket

ip = "127.0.0.1"
port = 8080

try:
    sock = socket.socket()
    sock.connect((ip, port))
    print(f"Port {port} is OPEN")
except ConnectionRefusedError as CRE:
    print(f"Port {port} is CLOSED. [Error: {CRE}]")
finally:
    sock.close()