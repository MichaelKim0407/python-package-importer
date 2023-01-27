from python_package_importer.importer import PythonPackageImporter


class TestPackageImporter:
    def test_call(self, example_package):
        importer = PythonPackageImporter(example_package)
        result = importer()
        assert isinstance(result, list)

    def test_basic(self, example_package):
        importer = PythonPackageImporter(example_package)
        assert {module.__name__ for module in importer} == {
            'tests.example_package.my_py_file',
        }

    def test_include_self(self, example_package):
        importer = PythonPackageImporter(example_package, include_self=True)
        assert {module.__name__ for module in importer} == {
            'tests.example_package',
            'tests.example_package.my_py_file',
        }

    def test_import_packages(self, example_package):
        importer = PythonPackageImporter(example_package, import_packages=True)
        assert {module.__name__ for module in importer} == {
            'tests.example_package.my_py_file',
            'tests.example_package.sub_package',
        }

    def test_recursive(self, example_package):
        importer = PythonPackageImporter(example_package, recursive=True)
        assert {module.__name__ for module in importer} == {
            'tests.example_package.my_py_file',
            'tests.example_package.sub_package',
            'tests.example_package.sub_package.sub_file',
        }
