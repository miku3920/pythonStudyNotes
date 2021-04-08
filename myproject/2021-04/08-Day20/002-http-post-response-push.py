from cgi import parse_header, parse_multipart
import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import parse_qs
import json
import requests

auth_token='???????'

class MyHandler(RequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):

        userId="????"
        varLen = int(self.headers['Content-Length'])
        if varLen > 0:
            post_data = self.rfile.read(varLen)
            data = json.loads(post_data)
            print(data)
            userId=data['events'][0]['source']['userId']

        self.do_HEAD()
        # print(self.wfile)
        message = {
            "to": str(userId),
            "messages": [
                {
                    "type": "text",
                    "text": "安安你好"
                },
                {
                    "type": "text",
                    "text": "賽馬娘神作"
                }
            ]
        }

        hed = {'Authorization': 'Bearer ' + auth_token}
        url = 'https://api.line.me/v2/bot/message/push'
        response = requests.post(url, json=message, headers=hed)
        print(response)
        print(response.json())


socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', 8000), MyHandler)
httpd.serve_forever()
