"""Signing keys.

The keys are not in this repo. They come from the environment, which is set
by the deployment.

IDENTITY_SIGNING_KEY   the current key, as "kid:secret"
IDENTITY_OLD_KEYS      earlier keys, still accepted, as "kid:secret,kid:secret"
"""

import os


def _parse(value):
    keys = {}
    for part in value.split(","):
        if ":" in part:
            kid, secret = part.split(":", 1)
            keys[kid.strip()] = secret.strip().encode()
    return keys


def _all_keys():
    keys = _parse(os.environ.get("IDENTITY_OLD_KEYS", ""))
    keys.update(_parse(os.environ.get("IDENTITY_SIGNING_KEY", "")))
    return keys


def current_kid():
    current = _parse(os.environ.get("IDENTITY_SIGNING_KEY", ""))
    if not current:
        raise RuntimeError("IDENTITY_SIGNING_KEY is not set")
    return next(iter(current))


def key_for(kid):
    return _all_keys().get(kid)
