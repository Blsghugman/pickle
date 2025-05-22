from utils.sample_objects import sample_objects
from utils.hasher import hash_pickle
import pickle


def test_pickle_output_by_version():
    print("\n=== Pickle Output for This Python Version ===\n")
    print(f"Python version: {pickle.__spec__.origin}")  # 显示 pickle 所在位置
    print(f"Pickle protocol: {pickle.HIGHEST_PROTOCOL}")
    print(f"sample_objects length: {len(sample_objects)}")  # DEBUG
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
