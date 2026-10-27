# gateway

The single entry point for the archive APIs.

For every request the gateway:

1. Finds the route in `config/routes.json`.
2. Verifies the token with RS256 against the identity service's public key.
3. Checks that the token has the scope the route needs, and returns 403 if not.
4. Forwards the request to the service with the user in `X-User-Id`.

Services behind the gateway don't need to check anything themselves.

Last updated: 2022.
