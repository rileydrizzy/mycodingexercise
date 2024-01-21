"""conftest.py
"""

import subprocess
import os
import pytest


@pytest.fixture
def test_data_folder():
    """_summary_

    Returns
    -------
    _type_
        _description_
    """
    return os.path.join(os.path.dirname(__file__), "tests")


@pytest.fixture
def run_code(test_data_folder):
    """_summary_

    Parameters
    ----------
    test_data_folder : _type_
        _description_
    """

    def _run_code(test_file):
        command = [
            "python",
            "check_brackets.py",
        ]
        test_file = os.path.join(test_data_folder, test_file)
        with open(test_file, "r", encoding="UTF-8") as input_file:
            result = subprocess.run(
                command,
                input=input_file.read(),
                check=True,
                capture_output=True,
                text=True,
            )
        return result.stdout.strip()

    return _run_code
