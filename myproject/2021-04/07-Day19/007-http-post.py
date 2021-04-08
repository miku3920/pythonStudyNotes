from sys import version as python_version
from cgi import parse_header, parse_multipart
import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import parse_qs
import json

class MyHandler(RequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_POST(self):
        varLen = int(self.headers['Content-Length'])
        if varLen>0:
            post_data = self.rfile.read(varLen)
            data = json.loads(post_data)
            print(data)
            name = data["name"]
            password = data["password"]

        self.do_HEAD()
        print(self.wfile)
        output = '<html><meta charset="utf-8"><body>Hello name='+name+'<br>'+password+'</body></html>'
        self.wfile.write(output.encode("utf-8"))

socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', 8888), MyHandler)
httpd.serve_forever()
