import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler

class MyHandler(RequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        output = "<html><body>你好，我是 miku3920</body></html>"
        self.wfile.write(output.encode("big5"))


socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', 8888), MyHandler)
httpd.serve_forever()