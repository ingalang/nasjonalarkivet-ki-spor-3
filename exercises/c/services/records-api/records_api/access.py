READ = "records:read"
READ_RESTRICTED = "records:read-restricted"


def can_see(caller, record):
    """Whether the caller may know the record exists at all."""
    if record["classification"] != "restricted":
        return True
    return READ_RESTRICTED in caller["scopes"] and caller["unit"] == record["owner_unit"]


def can_read(caller, record):
    return READ in caller["scopes"] and can_see(caller, record)
