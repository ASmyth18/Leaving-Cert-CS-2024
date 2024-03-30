import http.server
import requests
import cgi
import os  

url = 'http://109.76.70.34:80/C:/Users/adams/Desktop'
file_path = 'C:/Users/adams/Desktop/Firewall/firewall.log'

with open(file_path, 'rb') as file:
    files = {'file': file}
    response = requests.post(url, files=files)

print(response.status_code)
print(response.text)

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/upload':
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )
            file_item = form['file']
            if file_item.filename:
                file_path = os.path.join('uploads', file_item.filename)
                with open(file_path, 'wb') as f:
                    f.write(file_item.file.read())
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'File uploaded successfully')
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'No file was uploaded')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

if __name__ == '__main__':
    server_address = ('', 80)
    httpd = http.server.HTTPServer(server_address, CustomHTTPRequestHandler)
    print('Server running on port 80...')
    httpd.serve_forever()