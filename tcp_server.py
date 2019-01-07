import socket
import threading

bind_ip = "0.0.0.0" # the interface ip of the incomming connection
bind_port = 1234 # port to accept the connection

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port)) # bind in a port and interface ip
server.listen(5) # no of connection to accept

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

# this is our client-handling thread
# each thead runs the method client_handle and tools till data 
# us present and coming from the client

def handle_client(client_socket):
# print out what the client sends
    request = 1
    while request:
      request = client_socket.recv(1024)
      print "[*] Received: %s" % request.decode()
# send back a packet
      data = raw_input("Data to send back? ")
      client_socket.send(data.encode())
    client_socket.close()

while True:
  client,addr = server.accept()
  print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
# spin up our client thread to handle incoming data
  client_handler = threading.Thread(target=handle_client,args=(client,))
  client_handler.start()
