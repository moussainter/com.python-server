#coding:utf-8
import http.server


port = 80
address = ("", port)

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(address, handler)

print(f"Serving HTTP on port {port} ...")

httpd.serve_forever()