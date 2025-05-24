"""Autograding script."""

import os


def test_01():
    """Test"""

    assert os.path.exists("models1"), "models1/ directory does not exist"
    assert os.path.exists("homework/src"), "models1/ directory does not exist"
    assert os.path.exists(
        "models1/estimator.pkl"
    ), "models1/estimator.pkl file does not exist"
