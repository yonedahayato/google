import http.server
import socketserver

PORT = 8080
# Handler = http.server.SimpleHTTPRequestHandler

class ServerHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        with open("/var/log/sample.log", "w") as f:
            f.write("test")
        http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = ServerHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
