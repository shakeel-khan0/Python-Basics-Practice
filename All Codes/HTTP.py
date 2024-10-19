# Import the HTTP server module
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the port
PORT = 8080

# Create an HTTP server
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd on port {PORT}...")
    httpd.serve_forever()

# Run the server
if __name__ == "__main__":
    run()
