import pytest


@pytest.fixture(scope='session')
def example_package():
    from . import example_package
    return example_package
