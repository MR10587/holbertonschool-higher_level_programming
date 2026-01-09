#!/usr/bin/python3
import http.server


class handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b'Hello, this is a simple API!')

def run_server():
    server_address = ('', 8080)
    httpd = http.server.HTTPServer(server_address, handler)
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()