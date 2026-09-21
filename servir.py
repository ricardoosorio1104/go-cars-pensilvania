#!/usr/bin/env python3
"""
Servidor local para previsualizar el sitio de GO CARS Pensilvania.

Soporta peticiones HTTP Range (206 Partial Content). Es necesario porque los
videos del sitio AVANZAN CON EL SCROLL (scrub): el navegador necesita poder
pedir fragmentos del video. El `python -m http.server` normal NO soporta Range,
y con él los videos grandes se quedan congelados al desplazarse.

Uso:
    python servir.py            -> http://127.0.0.1:8099
    python servir.py 5000       -> otro puerto
"""
import http.server
import os
import re
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8099
ROOT = os.path.dirname(os.path.abspath(__file__))


class RangeHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            index = os.path.join(path, "index.html")
            if os.path.exists(index):
                path = index
            else:
                return super().send_head()
        if not os.path.isfile(path):
            self.send_error(404, "No encontrado")
            return None

        size = os.path.getsize(path)
        ctype = self.guess_type(path)
        start, end, partial = 0, max(size - 1, 0), False

        rng = self.headers.get("Range")
        if rng:
            m = re.match(r"bytes=(\d*)-(\d*)\s*$", rng.strip())
            if m and (m.group(1) or m.group(2)):
                if m.group(1):
                    start = int(m.group(1))
                    if m.group(2):
                        end = min(int(m.group(2)), size - 1)
                else:  # sufijo: bytes=-N  (últimos N bytes)
                    start = max(0, size - int(m.group(2)))
                if start > end:
                    start = 0
                partial = True

        f = open(path, "rb")
        f.seek(start)
        self.send_response(206 if partial else 200)
        self.send_header("Content-Type", ctype)
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Length", str(end - start + 1))
        if partial:
            self.send_header("Content-Range", "bytes %d-%d/%d" % (start, end, size))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        return f

    def log_message(self, fmt, *args):
        pass


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    with Server(("127.0.0.1", PORT), RangeHandler) as httpd:
        print("GO CARS Pensilvania -> http://127.0.0.1:%d  (Ctrl+C para salir)" % PORT)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nCerrado.")
