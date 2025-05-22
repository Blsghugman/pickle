"""
# Pickle Stability & Correctness Test Suite

This project tests whether Python's `pickle` module produces hash-identical serialized outputs across environments and conditions.

## Structure
- `tests/`: Contains all test modules.
- `utils/`: Helpers for object creation and hashing.
- `run_tests.py`: Entrypoint for running all tests.

## Setup
```bash
pip install -r requirements.txt
```

## Run
```bash
python run_tests.py
```

## Report Output
All test logs and hash mismatches are saved in `test_results/`.
"""
