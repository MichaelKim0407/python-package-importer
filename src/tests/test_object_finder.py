import re
import types

from python_package_importer.object_finder import PythonPackageObjectFinder


class TestObjectFinder:
    def test_call(self, example_package):
        finder = PythonPackageObjectFinder(example_package)
        result = finder()
        assert isinstance(result, list)

    def test_basic(self, example_package):
        finder = PythonPackageObjectFinder(example_package)
        assert set(finder) == {
            ('tests.example_package.my_py_file', 'v_int', example_package.my_py_file.v_int),
            ('tests.example_package.sub_package', 'v_str', example_package.sub_package.v_str),
            ('tests.example_package.sub_package.sub_file', 'C', example_package.sub_package.sub_file.C),
            ('tests.example_package.sub_package.sub_file', 'c', example_package.sub_package.sub_file.c),
        }

    def test_allow_magic_and_selector(self, example_package):
        finder = PythonPackageObjectFinder(
            example_package,
            selector=lambda name, obj: name == '__name__',
            allow_magic=True,
        )
        assert set(finder) == {
            ('tests.example_package', '__name__', example_package.__name__),
            ('tests.example_package.my_py_file', '__name__', example_package.my_py_file.__name__),
            ('tests.example_package.sub_package', '__name__', example_package.sub_package.__name__),
            ('tests.example_package.sub_package.sub_file', '__name__', example_package.sub_package.sub_file.__name__),
        }

    def test_include_submodules_and_obj_type(self, example_package):
        finder = PythonPackageObjectFinder(
            example_package,
            include_submodules=True,
            obj_type=types.ModuleType,
        )
        assert set(finder) == {
            ('tests.example_package', 'my_py_file', example_package.my_py_file),
            ('tests.example_package', 'sub_package', example_package.sub_package),
            ('tests.example_package.sub_package', 'sub_file', example_package.sub_package.sub_file),
        }

    def test_name_re(self, example_package):
        finder = PythonPackageObjectFinder(
            example_package,
            name_re=re.compile(r'v_.*'),
        )
        assert set(finder) == {
            ('tests.example_package.my_py_file', 'v_int', example_package.my_py_file.v_int),
            ('tests.example_package.sub_package', 'v_str', example_package.sub_package.v_str),
        }
