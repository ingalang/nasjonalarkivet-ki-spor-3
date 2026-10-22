"""Live dashboard for the answers in the survey-db Postgres container.

Run:  python3 survey/dashboard.py   (opens http://localhost:8001 in the browser)
Localhost only – the answers are not exposed through ngrok.
"""
import json
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import db

ROOT = Path(__file__).resolve().parent
PORT = 8001


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            self.reply(json.dumps(db.rows(), ensure_ascii=False), "application/json")
        else:
            self.reply((ROOT / "dashboard.html").read_text(encoding="utf-8"), "text/html")

    def reply(self, text, ctype):
        body = text.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", f"{ctype}; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    print(f"Dashboard on http://localhost:{PORT}")
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    webbrowser.open(f"http://localhost:{PORT}")
    server.serve_forever()
