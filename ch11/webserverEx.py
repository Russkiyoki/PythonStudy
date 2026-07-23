import socket

# Create a web server using the same socket concepts!
web_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
web_server.bind(("localhost", 8080))  # Listen on port 8080
web_server.listen(1)

print("Web server running! Visit http://localhost:8080")

while True:
    # Wait for a browser to connect
    browser, address = web_server.accept()
    
    # Read what the browser requested
    request = browser.recv(1024)
    print(f"Browser asked for: {request.split()[1]}")  # Shows the URL path
    
    # Send back a web page
    html_response = b"""HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>My Server</title>
</head>
<body>
    <h1>Hello from my custom web server!</h1>
    <p>This page was sent using Python sockets.</p>
    <p>The current time is: 12:00 PM</p>
</body>
</html>"""
    
    browser.send(html_response)
    browser.close()
