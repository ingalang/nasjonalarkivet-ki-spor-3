import json
import logging

from records_api import access, store
from records_api.trust import caller_from_gateway

log = logging.getLogger("records_api")


def _json(status, body):
    return status, {"Content-Type": "application/json"}, json.dumps(body).encode()


def get_record(record_id, headers):
    caller = caller_from_gateway(headers)
    if caller is None:
        return _json(401, {"error": "not from gateway"})

    record = store.find(record_id)
    if record is None or not access.can_see(caller, record):
        # Same answer as a missing record, so restricted records can't be discovered.
        return _json(404, {"error": "not found"})

    if not access.can_read(caller, record):
        log.info("denied %s to %s", record_id, caller["user_id"])
        return _json(403, {"error": "forbidden"})

    return _json(200, record)
