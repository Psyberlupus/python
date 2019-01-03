import socket
# Sample code for TCP or UDP client in python
# change target address and port

print "Enter target and port!!"
target_host = raw_input("Target hostname: ")
target_port = raw_input("Port?  ")
target_port = int(target_port
if not target_host:
   target_host = "127.0.0.1" # provide a hostname
if not target_port:
   target_port = 1234 # provide a port to connect
print "TCP or UDP socket client!!"
TCP = raw_input("Enter 1 for TCP and 0 for UDP connection:  ")
# create a socket object
if TCP:
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client.connect((target_host, target_port))
   # We connect to the remote port if TCP connection
if not TCP:
   client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   # Notice UDP is connectionless hence to call to connect()
response = 1
while response:
  msg = raw_input("Data to send: ")
  if TCP:
     client.send(msg.encode())
     response = client.recv(1024)
  if not TCP: 
     client.sendto(msg,(target_host, target_port))
     response, addr = client.recvfrom(4096)
  print response.decode()
client.close()
