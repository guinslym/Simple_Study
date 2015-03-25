#! /usr/bin/env/python

if __name__ == '__main__':
	import sys
	import CGIHTTPServer
    import BaseHTTPServer
	server = BaseHTTPServer.HTTPServer
	handler = CGIHTTPServer.CGIHTTPRequestHandler
	server_address = ("",int(sys.argv[1]))
	handler.cgi_directories = ['/cgi-bin','/cgi-bin/subdir']
	httpd = server(server_address,handler)
	httpd.serve_forever()