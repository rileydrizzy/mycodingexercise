"""doc
"""

import os
import subprocess
import pytest


@pytest.fixture
def test_folder():
    return os.path.join(os.path.dirname(__file__), "tests")


@pytest.fixture
def run_code(test_folder):
    def inner_run_code(test_file):
        command = ["python", "process_packages.py"]
        test_file = os.path.join(test_folder, test_file)
        with open(test_file, "r", encoding="UTF-8") as input_file:
            result = subprocess.run(
                command,
                input=input_file.read(),
                check=True,
                capture_output=True,
                text=True,
            )
        return result.stdout.strip()

    return inner_run_code
