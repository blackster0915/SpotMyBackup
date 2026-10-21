# Serves SpotMyBackup on http://127.0.0.1:8888.
# Spotify only accepts the loopback IP as redirect URI, not "localhost".
import functools
import http.server
import os

# index.html and login.html load config.json with a <script> tag
http.server.SimpleHTTPRequestHandler.extensions_map['.json'] = 'application/javascript'

handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=os.path.dirname(os.path.abspath(__file__)))
with http.server.ThreadingHTTPServer(('127.0.0.1', 8888), handler) as httpd:
    print('SpotMyBackup runs on http://127.0.0.1:8888 - close this window to stop it.')
    httpd.serve_forever()
