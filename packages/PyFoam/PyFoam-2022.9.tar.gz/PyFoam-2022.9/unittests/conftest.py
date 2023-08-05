"""Global fixtures"""

import pytest

from os import path


@pytest.fixture
def data_directory():
    """Path to the directory with test data."""
    return path.join(path.dirname(__file__), path.pardir, "testdata")


@pytest.fixture
def empty_case(data_directory):
    """Path to an empty case."""
    return path.join(data_directory, "empty_case")
