"""Issue and verify access tokens.

Format: base64url(header).base64url(claims).base64url(signature)
The signature is HMAC-SHA256 over "header.claims" with the key named by "kid".
"""

import base64
import hashlib
import hmac
import json
import time

from identity.keys import current_kid, key_for

AUDIENCE = "arkiv-api"
TTL_SECONDS = 900
LEEWAY_SECONDS = 30


class TokenError(Exception):
    pass


def _b64(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def _unb64(text):
    return base64.urlsafe_b64decode(text + "=" * (-len(text) % 4))


def issue(user_id, scopes, unit):
    kid = current_kid()
    header = {"alg": "HS256", "kid": kid}
    now = int(time.time())
    claims = {
        "sub": user_id,
        "aud": AUDIENCE,
        "iat": now,
        "exp": now + TTL_SECONDS,
        "scope": " ".join(scopes),
        "unit": unit,
    }
    signing_input = _b64(json.dumps(header).encode()) + "." + _b64(json.dumps(claims).encode())
    sig = hmac.new(key_for(kid), signing_input.encode(), hashlib.sha256).digest()
    return signing_input + "." + _b64(sig)


def verify(token):
    try:
        header_b64, claims_b64, sig_b64 = token.split(".")
        header = json.loads(_unb64(header_b64))
        claims = json.loads(_unb64(claims_b64))
    except ValueError as e:
        raise TokenError("malformed token") from e

    if header.get("alg") != "HS256":
        raise TokenError("unsupported alg")
    key = key_for(header.get("kid"))
    if key is None:
        raise TokenError("unknown kid")

    expected = hmac.new(key, (header_b64 + "." + claims_b64).encode(), hashlib.sha256).digest()
    if not hmac.compare_digest(expected, _unb64(sig_b64)):
        raise TokenError("bad signature")

    if claims.get("exp", 0) + LEEWAY_SECONDS < time.time():
        raise TokenError("expired")
    if claims.get("aud") != AUDIENCE:
        raise TokenError("wrong audience")
    return claims
