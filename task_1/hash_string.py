import hashlib


def hash_func(text: str):
    """Calculates SHA1 hash of the provided string"""
    hash_object = hashlib.sha1(text.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig


s = "Hello World"
# print(hash_func(s))
