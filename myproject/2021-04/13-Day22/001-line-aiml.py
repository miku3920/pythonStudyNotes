import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import parse_qs
import json
import requests
import aiml

kernel = aiml.Kernel()
kernel.learn("AIML.xml")

auth_token = '?????????'


class MyHandler(RequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        varLen = int(self.headers['Content-Length'])
        if varLen > 0:
            post_data = self.rfile.read(varLen)
            data = json.loads(post_data)
            print(data)
            replyToken = data['events'][0]['replyToken']
            # userId=data['events'][0]['source']['userId']
            text = data['events'][0]['message']['text']

        self.do_HEAD()

        reply_text = kernel.respond(text)
        if reply_text:
            message = {
                "replyToken": replyToken,
                "messages": [
                    {
                        "type": "text",
                        "text": reply_text
                    }
                ]
            }

            hed = {'Authorization': 'Bearer ' + auth_token}
            url = 'https://api.line.me/v2/bot/message/reply'
            response = requests.post(url, json=message, headers=hed)
            print(response)
            print(response.json())


socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', 8000), MyHandler)
httpd.serve_forever()
