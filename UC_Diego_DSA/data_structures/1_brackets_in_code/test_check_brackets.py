"""test_your_code.py
"""
import os


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
    for test_file in range(1, 55):
        output = run_code(str(test_file))
        expected_file = str(test_file) + ".a"

        with open(
            os.path.join(test_data_folder, expected_file), "r", encoding="UTF-8"
        ) as expected:
            expected_output = expected.read().strip()
        assert (
            output == expected_output
        ), f"Test {test_file} failed. Expected: {expected_output}, Got: {output}"
