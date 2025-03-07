import time


def generate_timestamp():
    """
    Return a millisecond integer timestamp.
    """
    return int(time.time() * 10**3)


def find_index(source, target, key):
    """
    Find the index in source list of the targeted ID.
    """
    return next(i for i, j in enumerate(source) if j[key] == target[key])
