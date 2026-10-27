"""In-memory stand-in for the records database."""

RECORDS = {
    "rec-1001": {"id": "rec-1001", "title": "Board minutes 1987", "classification": "open", "owner_unit": "RA"},
    "rec-1002": {"id": "rec-1002", "title": "Personnel file 4412", "classification": "restricted", "owner_unit": "SAO"},
}


def find(record_id):
    return RECORDS.get(record_id)
