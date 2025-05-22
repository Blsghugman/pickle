import pytest
from utils.sample_objects import sample_objects
from utils.hasher import hash_pickle

print("Loaded test_equivalence.py")


@pytest.mark.parametrize("obj", sample_objects)
def test_equivalence_class(obj):
    hashed = hash_pickle(obj, protocol=5)
    print(f"Type: {type(obj).__name__}")
    print(f"Repr: {repr(obj)}")
    print(f"Hash: {hashed}")
    print("-" * 60)
