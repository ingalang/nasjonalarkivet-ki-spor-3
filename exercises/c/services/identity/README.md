# identity

Issues access tokens for the archive APIs.

- `identity/tokens.py` issues and verifies tokens (HMAC-SHA256, 15 minutes).
- `identity/keys.py` reads the signing keys from the environment.

Other services should call `tokens.verify()` to check a token. Don't copy it.
