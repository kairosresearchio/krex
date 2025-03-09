import time
from datetime import datetime, timezone


def generate_timestamp(iso_format=False):
    if iso_format:
        return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    return int(time.time() * 10**3)
