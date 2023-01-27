from python_package_importer.pytest import PytestFixturePackageLoader
from . import fixtures

PytestFixturePackageLoader(fixtures)(locals())
