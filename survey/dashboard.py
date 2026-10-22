"""Live-dashboard for svar.jsonl.

Kjør:  python3 survey/dashboard.py   (åpner http://localhost:8001 i nettleseren)
Kun localhost – svarene eksponeres ikke via ngrok.
"""
import json
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "svar.jsonl"
PORT = 8001


def read_rows():
    if not OUT.exists():
        return []
    rows = []
    for line in OUT.read_text(encoding="utf-8").splitlines():
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            pass  # halvskrevet linje, kommer med neste runde
    return rows


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            self.reply(json.dumps(read_rows(), ensure_ascii=False), "application/json")
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
    print(f"Dashboard på http://localhost:{PORT}")
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    webbrowser.open(f"http://localhost:{PORT}")
    server.serve_forever()
