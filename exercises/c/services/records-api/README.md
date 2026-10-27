# records-api

Serves archive records: `GET /records/<id>`.

## Authentication

records-api verifies the bearer token itself with `identity.tokens.verify()`
(see `records_api/legacy_jwt.py`) and needs the scope `records:read`.

Restricted records return 403 if you are not allowed to read them.
