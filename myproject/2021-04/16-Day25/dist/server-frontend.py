import socketserver as socketserver
from http.server import SimpleHTTPRequestHandler as RequestHandler

socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', 80), RequestHandler)
print('server is on')
httpd.serve_forever()
