#!/usr/bin/python3
import http.server
import socketserver


dataset = {"name": "John", "age": 30, "city": "New York"}
to_json = json.dumps(dataset)

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            
            self.wfile.write(to_json.encode())
        
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            
            self.wfile.write(b'OK')
        
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(b'Endpoint not found')
        

httpd = socketserver.TCPServer(("", 9990), Handler)
httpd.serve_forever()