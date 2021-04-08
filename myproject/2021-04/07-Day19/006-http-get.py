import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import urlparse
from urllib.parse import unquote

class MyHandler(RequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        name=""
        password=""
        query = unquote(urlparse(self.path).query)
        if query != "":
            query_components = dict(qc.split("=") for qc in query.split("&"))
            name = query_components["name"]
            password = query_components["password"]
        self.do_HEAD()
        output = '<html><meta charset="utf-8"><body>Hello name='+name+'<br>'+password+'</body></html>'
        self.wfile.write(output.encode("utf-8"))


socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', 8888), MyHandler)
httpd.serve_forever()
