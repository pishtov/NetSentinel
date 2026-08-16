# Port Probe

A minimal command-line tool to check whether a single TCP port is open on a given host.

## Requirements

- Python 3.6+
- No external dependencies (uses only the standard library)

## Usage

```bash
python port_probe.py [host] [-p PORT]
```

### Arguments

| Argument         | Description                          | Default     |
|------------------|---------------------------------------|-------------|
| `host`           | Target IP address or hostname         | `127.0.0.1` |
| `-p`, `--port`   | Target port number                    | `8080`      |

### Examples

Check if port 8080 is open on localhost:
```bash
python port_probe.py
```

Check if HTTPS (443) is open on a specific host:
```bash
python port_probe.py example.com -p 443
```

Check a port on a specific IP:
```bash
python port_probe.py 192.168.1.1 -p 22
```

## Exit Codes

The script sets its exit code based on the result, so it's easy to use in shell scripts and conditionals:

| Code | Meaning                          |
|------|-----------------------------------|
| `0`  | Port is open                     |
| `1`  | Port is closed                   |
| `2`  | Connection attempt timed out     |
| `3`  | Other network/OS error occurred  |

### Example in a shell script

```bash
if python port_probe.py example.com -p 443; then
    echo "HTTPS is reachable"
else
    echo "HTTPS is not reachable"
fi
```

## How It Works

The script opens a TCP socket and attempts to connect to the specified host and port using a 2-second timeout. It uses `socket.connect_ex()`, which returns an error code rather than raising an exception, to determine whether the connection succeeded.

## Notes

- This tool checks **one host and one port at a time** — it does not scan ranges or multiple hosts.
- The default timeout is 2 seconds and is not currently exposed as a command-line option.
- Only use this against hosts and networks you own or have explicit permission to test.