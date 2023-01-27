from python_package_importer.pytest import PytestFixturePackageLoader


class TestFixtureLoader:
    def test(self):
        from . import fixtures
        from .fixtures import example_package
        d = {}
        PytestFixturePackageLoader(fixtures)(d)
        assert d == {
            'example_package': example_package,
        }
