# server.py
import http.server
import socketserver
from urllib.parse import urlparse

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(302)
            self.send_header('Location', '/home/')
            self.end_headers()
        else:
            super().do_GET()

with socketserver.TCPServer(("", 8080), Handler) as httpd:
    print("Serving at http://localhost:8080")
    httpd.serve_forever()
