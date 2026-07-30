## What is an IP address?
An IP (Internet Protocol) address is a numerical identifier assigned to a network interface on a device. It allows devices to send and receive network packets, enabling communication over a network.

### Why does NetSentinel need an IP address?
The scanner must know the address of the target device before it can attempt to connect to a TCP port. 
If the user provides a hostname (e.g., google.com), it must first be 
resolved to an IP address through DNS (`Domain Name System`) before a connection can be attempted.

## What is port?
A port is a numerical identifier that represents a specific network service or application running on a device. Together with an IP 
address, it tells the operating system which application or service should receive incoming network traffic.

### Why does NetSentinel need ports?
NetSentinel scans ports to determine which services are listening for incoming connections on a target device. An open port usually indicates that a network service, such as a web server or an SSH server, is available and accepting connections.

### What does it actually mean for a port to be "open" ?
An open port is a port on which a network service is listening for incoming connection requests.

## What is a socket?
A socket is an operating system object that represents one end of a network connection and allows a program to send and receive data.

### Is NetSentinel a client or a server?
NetSentinel behaves as a client. It initiates TCP connections to a target IP address and port in order to determine whether a service is listening. The target service acts as the server by waiting for and responding to incoming connection requests.