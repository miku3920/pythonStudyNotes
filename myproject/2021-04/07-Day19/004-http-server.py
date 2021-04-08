import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler

socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', 8888), RequestHandler)
httpd.serve_forever()