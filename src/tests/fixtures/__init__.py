import pytest


@pytest.fixture(scope='session')
def example_package():
    from tests import example_package
    return example_package
