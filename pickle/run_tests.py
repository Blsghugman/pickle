import pytest
import os

if __name__ == "__main__":
    os.makedirs("test_results", exist_ok=True)
    pytest.main(["-v", "tests/", "--tb=short", "--maxfail=5", "--capture=tee-sys", f"--junitxml=test_results/report.xml"])
