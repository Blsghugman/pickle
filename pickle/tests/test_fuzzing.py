from hypothesis import given
import hypothesis.strategies as st
from utils.hasher import hash_pickle

print("Loaded test_fuzzing.py")


@given(st.integers())
def test_fuzz_integers(val):
    hashed = hash_pickle(val)
    print(f"Fuzz int: {val}, Hash: {hashed}")


@given(st.lists(st.integers(), max_size=100))
def test_fuzz_lists(val):
    hashed = hash_pickle(val)
    print(f"Fuzz list: {val}, Hash: {hashed}")
