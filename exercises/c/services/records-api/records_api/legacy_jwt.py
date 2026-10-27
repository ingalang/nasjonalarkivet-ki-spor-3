"""Token check from before the gateway.

records-api used to verify tokens itself. Kept in case we need to run
without the gateway again.
"""

from identity.tokens import TokenError, verify


def caller_from_token(headers):
    value = headers.get("Authorization", "")
    if not value.startswith("Bearer "):
        return None
    try:
        claims = verify(value[len("Bearer "):])
    except TokenError:
        return None
    return {
        "user_id": claims["sub"],
        "scopes": set(claims.get("scope", "").split()),
        "unit": claims.get("unit", ""),
    }
