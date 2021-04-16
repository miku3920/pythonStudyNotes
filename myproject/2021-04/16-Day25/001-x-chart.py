# project 5
import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import urlparse
from urllib.parse import unquote
import json


class MyHandler(RequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        path = unquote(urlparse(self.path).path)
        self.do_HEAD()
        data = ['error']
        if path == '/dashboard':
            data = self.get_dashboard()
        elif path == '/chart_data':
            query = unquote(urlparse(self.path).query)
            if query:
                query_components = dict(qc.split("=") for qc in query.split("&"))
                if 'q' in query_components:
                    q=query_components["q"]
                    q=self.fix_q(q)
            data = self.get_chart_data()
        output = json.dumps(data)
        self.wfile.write(output.encode("utf-8"))

    def fix_q(self,q):
        d={
            '中壢':'中壢區'
        }
        if q in d:
            return d[q]
        else:
            return False

    def get_dashboard(self):
        return {
            "slices": [
                {
                    "sliceId": 1,
                    "x": 0,
                    "y": 0,
                    "w": 36,
                    "h": 14,
                    "width": 360,
                    "height": 290,
                    "i": "chart1",
                    "chartType": "x-line-area",
                    "title": "Line Area"
                }
            ]
        }

    def get_chart_data(self):
        return{
            "chartType": "x-line-area",
            "columns": [
                {
                    "type": "x",
                    "field": "course_name",
                    "name": "Course Name"
                },
                {
                    "type": "y",
                    "field": "difficulty",
                    "name": "Enrols"
                }
            ],
            "rows": [
                {
                    "difficulty": 9408.81,
                    "course_name": "Course1"
                },
                {
                    "difficulty": 8024.02,
                    "course_name": "Course2"
                },
                {
                    "difficulty": 7729.59,
                    "course_name": "Course3"
                },
                {
                    "difficulty": 6430.59,
                    "course_name": "Course4"
                },
                {
                    "difficulty": 6140.94,
                    "course_name": "Course5"
                },
                {
                    "difficulty": 6065.3,
                    "course_name": "Course6"
                },
                {
                    "difficulty": 6025.71,
                    "course_name": "Course7"
                },
                {
                    "difficulty": 4780.8,
                    "course_name": "Course8"
                },
                {
                    "difficulty": 4724.57,
                    "course_name": "Course9"
                },
                {
                    "difficulty": 4634.27,
                    "course_name": "Course10"
                }
            ]
        }


socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', 8000), MyHandler)
httpd.serve_forever()
