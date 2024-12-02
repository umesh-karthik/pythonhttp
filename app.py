import http.server
import socketserver

# Define the handler to serve the HTML file
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'  # Serve the index.html file when requested
        return super().do_GET()

# Set the port for the server (e.g., 8000)
PORT = 8000

# Create a TCP socket server that serves HTTP requests
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
