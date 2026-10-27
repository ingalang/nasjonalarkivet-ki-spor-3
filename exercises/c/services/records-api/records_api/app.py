import re

from records_api import handlers

RECORD = re.compile(r"^/records/([A-Za-z0-9-]+)$")


def handle(method, path, headers):
    """Returns (status, headers, body)."""
    if path == "/health":
        return 200, {}, b"ok"

    m = RECORD.match(path)
    if m and method == "GET":
        return handlers.get_record(m.group(1), headers)

    return 404, {}, b"not found"
