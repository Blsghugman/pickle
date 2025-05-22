from utils.hasher import hash_pickle
from utils.sample_objects import sample_objects
import pytest

print("Loaded test_protocol_versions.py")


@pytest.mark.parametrize("obj", sample_objects)
def test_protocol_variants(obj):
    print(f"\nObject Type: {type(obj).__name__}")
    print(f"Repr: {repr(obj)}")

    for i in range(6):
        try:
            h = hash_pickle(obj, protocol=i)
            print(f"  Protocol {i} → Hash: {h}")
        except Exception as e:
            print(f"  Protocol {i} → ERROR: {e}")
