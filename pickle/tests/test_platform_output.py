import platform
from utils.sample_objects import sample_objects
from utils.hasher import hash_pickle
import pickle


def test_pickle_output_by_platform():
    print("\n=== System Info ===\n")
    print(f"OS: {platform.system()}")  # Windows / Linux / Darwin (macOS)
    print(f"OS Version: {platform.version()}")
    print(f"Platform: {platform.platform()}")
    print(f"Architecture: {platform.architecture()[0]}")
    print("-" * 60)

    for idx, obj in enumerate(sample_objects):
        try:
            hashed = hash_pickle(obj)
            print(f"[{idx}] Type: {type(obj).__name__}")
            print(f"     Repr: {repr(obj)}")
            print(f"     Hash: {hashed}")
        except Exception as e:
            print(f"[{idx}] ERROR: Could not pickle object of type {type(obj)}")
            print(f"     Reason: {e}")

        print("-" * 60)
