import socket
import argparse
import sys

def check_port(host: str, port: int, timeout: float = 2.0) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((host, port)) == 0

def main():
    p = argparse.ArgumentParser(description="Simple port probe")
    p.add_argument("host", nargs="?", default="127.0.0.1", help="Target IP or hostname") # CHANGE THIS
    p.add_argument("-p", "--port", type=int, default=8080, help="Target port")           # CHANGE THIS
    args = p.parse_args()

    try:
        is_open = check_port(args.host, args.port)
    except socket.timeout:
        print(f"Port {args.port} on {args.host} timed out")
        sys.exit(2)
    except OSError as e:
        print(f"Error checking port {args.port} on {args.host}: {e}")
        sys.exit(3)

    if is_open:
        print(f"Port {args.port} on {args.host} is OPEN")
        sys.exit(0)
    else:
        print(f"Port {args.port} on {args.host} is CLOSED")
        sys.exit(1)

if __name__ == "__main__":
    main()