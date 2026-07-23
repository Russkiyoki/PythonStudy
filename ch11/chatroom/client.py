# AI GENERATED, NOT MY CODE AND IS TO BE LEARNED FROM
import socket

# 1. Create walkie-talkie
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Call the base station
s.connect(("192.168.1.10", 5000))  # Their IP address and port

# 3. Talk
while True:
    msg = input("You: ")
    s.send(msg.encode())  # Convert text to bytes
    if msg == "bye":
        break

s.close()
