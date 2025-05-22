from utils.hasher import hash_pickle

print("Loaded test_boundary.py")


def test_large_float():
    big_float = 1.7976931348623157e+308
    hashed = hash_pickle(big_float)
    print("Large float hash:", hashed)


def test_long_string():
    long_str = "a" * 10 ** 6
    hashed = hash_pickle(long_str)
    print("Long string hash:", hashed)
