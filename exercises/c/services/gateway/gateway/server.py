import json
import pathlib
import urllib.error
import urllib.request

from gateway.auth import AuthError, authenticate, upstream_headers

CONFIG = json.loads((pathlib.Path(__file__).parent.parent / "config" / "routes.json").read_text())


def find_route(path):
    for route in CONFIG["routes"]:
        if path.startswith(route["prefix"]):
            return route
    return None


def is_public(path):
    return any(path.startswith(p) for p in CONFIG["public_paths"])


def handle(method, path, headers):
    """Returns (status, headers, body)."""
    route = find_route(path)
    if route is None:
        return 404, {}, b"not found"

    if is_public(path):
        forward = dict(headers)
        forward.pop("Authorization", None)
    else:
        try:
            claims = authenticate(headers)
        except AuthError as e:
            out = {"WWW-Authenticate": 'Bearer error="invalid_token"'} if e.status == 401 else {}
            return e.status, out, e.reason.encode()
        forward = upstream_headers(headers, claims)

    url = route["upstream"] + path[len(route["prefix"]):]
    req = urllib.request.Request(url, method=method, headers=forward)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status, dict(resp.headers), resp.read()
    except urllib.error.HTTPError as e:
        # Pass the upstream status and body through unchanged.
        return e.code, dict(e.headers), e.read()
    except urllib.error.URLError:
        return 502, {}, b"bad gateway"
