import pytest
import pickle
from utils.sample_objects import sample_objects

print("Loaded test_roundtrip.py")


@pytest.mark.parametrize("obj", sample_objects)
def test_pickle_roundtrip(obj):
    try:
        serialized = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
        deserialized = pickle.loads(serialized)
        print(f"✅ [PASSED] {type(obj).__name__}")
        print(f"    Original repr: {repr(obj)}")
        print(f"    After loads(): {repr(deserialized)}")
        print("-" * 60)
    except Exception as e:
        print(f"❌ [FAIL] {type(obj).__name__} - {e}")
        print("-" * 60)
