import os
import sys
import http.server
import socketserver

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        path = http.server.SimpleHTTPRequestHandler.translate_path(self, path)
        if os.path.isdir(path):
            index = path + "/index.json"
            if os.path.exists(index):
                return index
        return path

with socketserver.TCPServer(("", 8000), MyHTTPRequestHandler) as httpd:
    print("Server started at http://localhost:8000")
    httpd.serve_forever()

