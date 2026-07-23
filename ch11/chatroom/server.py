# AI GENERATED, NOT MINE AND IS USED FOR LEARNING
import socket

# 1. Create the walkie-talkie
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Set your frequency (port 5000)
server.bind(("0.0.0.0", 5000))  # Listen on ALL network interfaces

# 3. Announce you're ready to receive
server.listen(1)  # Can handle 1 person waiting to connect

print("Waiting for someone to call...")

# 4. Wait for someone to connect (like answering a phone)
client, addr = server.accept()  # BLOCKS until someone connects
print(f"Connected to {addr}")

# 5. Keep talking
while True:
    msg = client.recv(1024)  # Listen for up to 1024 bytes
    if not msg:  # If connection lost
        break
    print(f"Them: {msg.decode()}")  # Convert bytes to text

client.close()
