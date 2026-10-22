"""Receives answers from the /survey skill.

Run:  python3 survey/server.py   and in another window:  ngrok http --url=uniambic-kamari-unbarrelled.ngrok-free.dev 8000
The answers end up in the answers table in the survey-db Postgres container (see README).
"""
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

import db

SKJEMA = "spor3-oslo-v1"
KEYS = ["id", "Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]
MAX_BYTES = 4096


def parse_md(text):
    d = {}
    for line in text.splitlines():
        if line.startswith("# Tilbakemelding "):
            d["id"] = line.removeprefix("# Tilbakemelding ").strip()
        elif ":" in line:
            k, v = line.split(":", 1)
            d[k.strip()] = v.strip()
    return d


def clean(d):
    if d.get("skjema") != SKJEMA:
        return None
    r = {k: str(d.get(k, "")).strip()[:1000] for k in KEYS}
    if not all(r[k] for k in ["Q1", "Q2", "Q3", "Q4"]):
        return None
    return r


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        n = int(self.headers.get("Content-Length") or 0)
        if n > MAX_BYTES:
            return self.reply(413, "For stort")
        self.save(parse_md(self.rfile.read(n).decode("utf-8", "replace")))

    def do_GET(self):
        q = {k: v[0] for k, v in parse_qs(urlparse(self.path).query).items()}
        if not q:
            return self.reply(200, "Spor 3 – tilbakemelding")
        self.save(q)

    def save(self, d):
        r = clean(d)
        if not r:
            return self.reply(400, "Ugyldig skjema")
        try:
            db.insert({"id": r["id"], "schema": SKJEMA, **{k.lower(): r[k] for k in KEYS[1:]}})
        except subprocess.CalledProcessError as e:
            print("Insert failed:", e.stderr.strip())
            return self.reply(500, "Kunne ikke lagre svaret")
        print("Received", r["id"])
        self.reply(200, "Takk for tilbakemeldingen!")

    def reply(self, code, msg):
        body = msg.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass  # don't log IP addresses


if __name__ == "__main__":
    db.init()
    print("Listening on http://localhost:8000")
    HTTPServer(("", 8000), Handler).serve_forever()
