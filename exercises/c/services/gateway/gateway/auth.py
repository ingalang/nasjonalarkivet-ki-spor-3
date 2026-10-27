import logging
import os

from gateway.vendor.identity_tokens import TokenError, verify

log = logging.getLogger("gateway.auth")

# Headers the gateway sets itself. Anything the client sends with these names is dropped.
TRUSTED_HEADERS = ("X-User-Id", "X-Scopes", "X-Unit", "X-Gateway-Secret")


class AuthError(Exception):
    def __init__(self, status, reason):
        super().__init__(reason)
        self.status = status
        self.reason = reason


def bearer_token(headers):
    value = headers.get("Authorization", "")
    if not value.startswith("Bearer "):
        raise AuthError(401, "missing bearer token")
    return value[len("Bearer "):]


def authenticate(headers):
    token = bearer_token(headers)
    try:
        claims = verify(token)
    except TokenError as e:
        log.info("token rejected: %s", e)
        raise AuthError(401, "invalid token")

    # TODO: check scopes per route here. Done in the services for now.
    # if not route_allows(claims["scope"]):
    #     raise AuthError(403, "insufficient scope")

    return claims


def upstream_headers(client_headers, claims):
    headers = {k: v for k, v in client_headers.items() if k not in TRUSTED_HEADERS}
    headers.pop("Authorization", None)
    headers["X-User-Id"] = claims["sub"]
    headers["X-Scopes"] = claims.get("scope", "")
    headers["X-Unit"] = claims.get("unit", "")
    headers["X-Gateway-Secret"] = os.environ.get("GATEWAY_SHARED_SECRET", "")
    return headers
