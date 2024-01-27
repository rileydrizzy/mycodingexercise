"""rteas
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
            "job_queue.py",
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


def test_run_code(run_code, test_data_folder):
    """_summary_

    Parameters
    ----------
    run_code : _type_
        _description_
    test_data_folder : _type_
        _description_
    """
    # Assuming you have test files 1, 2, etc.
    for test_file in range(1, 3):
        output = run_code(str(test_file))
        expected_file = str(test_file) + ".a"

        with open(
            os.path.join(test_data_folder, expected_file), "r", encoding="UTF-8"
        ) as expected:
            expected_output = expected.read().strip()
        assert (
            output == expected_output
        ), f"Test {test_file} failed. Expected: {expected_output}, Got: {output}"
