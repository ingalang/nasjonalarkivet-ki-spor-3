import os


def caller_from_gateway(headers):
    """Return the caller the gateway vouches for, or None.

    The gateway puts a shared secret in X-Gateway-Secret. Without it we can't
    trust X-User-Id and the rest.
    """
    expected = os.environ.get("GATEWAY_SHARED_SECRET", "")
    if headers.get("X-Gateway-Secret", "") != expected:
        return None
    return {
        "user_id": headers.get("X-User-Id"),
        "scopes": set(headers.get("X-Scopes", "").split()),
        "unit": headers.get("X-Unit", ""),
    }
