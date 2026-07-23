import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# stream based protocol via TCP via the af_inet
my_socket.connect(("www.example.com", 80))
my_socket.send(b"GET / HTTP/1.1\r\nHost:www.example.com\r\n\r\n")

# receving the actual data
response = my_socket.recv(4096)
# 4096 is the maximum bytes size 
print(response.decode())
my_socket.close()

