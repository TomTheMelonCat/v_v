import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class Local_Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        self.path = os.path.join(os.path.dirname(sys.modules['__main__'].__file__), 'items_display.html')
        try:
            file_to_open = open(self.path, encoding='utf-8').read()
            self.send_response(200)
        except:
            file_to_open = "Invalid file."
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(urllib.parse.unquote(file_to_open), 'utf-8'))


if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8080), Local_Serv)
    httpd.serve_forever()
