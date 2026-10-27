# Copied from identity/tokens.py in 2023 so the gateway doesn't need the
# identity package at runtime. Keep in sync by hand.

import base64
import hashlib
import hmac
import json
import os
import time

# Raised from 30 after clock problems on the old gateway hosts.
LEEWAY_SECONDS = 300


class TokenError(Exception):
    pass


def _unb64(text):
    return base64.urlsafe_b64decode(text + "=" * (-len(text) % 4))


def _keys():
    keys = {}
    for name in ("IDENTITY_OLD_KEYS", "IDENTITY_SIGNING_KEY"):
        for part in os.environ.get(name, "").split(","):
            if ":" in part:
                kid, secret = part.split(":", 1)
                keys[kid.strip()] = secret.strip().encode()
    return keys


def verify(token):
    try:
        header_b64, claims_b64, sig_b64 = token.split(".")
        header = json.loads(_unb64(header_b64))
        claims = json.loads(_unb64(claims_b64))
    except ValueError as e:
        raise TokenError("malformed token") from e

    if header.get("alg") != "HS256":
        raise TokenError("unsupported alg")
    key = _keys().get(header.get("kid"))
    if key is None:
        raise TokenError("unknown kid")

    expected = hmac.new(key, (header_b64 + "." + claims_b64).encode(), hashlib.sha256).digest()
    if not hmac.compare_digest(expected, _unb64(sig_b64)):
        raise TokenError("bad signature")

    if claims.get("exp", 0) + LEEWAY_SECONDS < time.time():
        raise TokenError("expired")
    return claims
