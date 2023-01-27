# python-package-importer

[![Release Status](https://github.com/MichaelKim0407/python-package-importer/actions/workflows/python-publish.yml/badge.svg)](https://github.com/MichaelKim0407/python-package-importer/releases)
[![PyPI package](https://badge.fury.io/py/python-package-importer.svg)](https://pypi.org/project/python-package-importer)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/python-package-importer)](https://pypi.org/project/python-package-importer)
[![Build Status](https://github.com/MichaelKim0407/python-package-importer/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/MichaelKim0407/python-package-importer/tree/main)
[![Coverage Status](https://coveralls.io/repos/github/MichaelKim0407/python-package-importer/badge.svg?branch=main)](https://coveralls.io/github/MichaelKim0407/python-package-importer?branch=main)

Utility for dynamically importing a Python package.

## Installation

```bash
pip install python-package-importer
```

## Usage

### class `python_package_importer.importer.PythonPackageImporter`

Import all modules and optionally sub-packages inside a package folder.

* `__init__(
    package,
    *,
    include_self=False,
    import_packages=False,
    recursive=False,
    )`

    * `package: types.ModuleType`:
        A reference to the package you would like to import.
        You will likely need to `import` it first (without needing to import everything within the package).

    * `include_self: bool = False`:
        Include a reference to `package` when returning results.

    * `import_packages: bool = False`:
        Import top-level packages (folders with `__init__.py`) under `package`. Ignored if `recursive`.

    * `recursive: bool = False`:
        Recursively import all sub-packages.

* `__iter__() -> typing.Iterator[types.ModuleType]`

    Iterate through all modules found in the package.
    Each module will be imported before it is iterated.

* `__call__() -> typing.List[types.ModuleType]`

    Return a list of all modules found in the package and import all of them.

Example:

```python
from python_package_importer.importer import PythonPackageImporter
import my_package  # <--- This is the package you would like to import

importer = PythonPackageImporter(
    my_package,
    recursive=True,
)
importer()  # <--- Import all under `my_package`
```

### class `python_package_importer.object_finder.PythonPackageObjectFinder`

Find all matching variables in all modules inside a package.

* `__init__(
    package,
    selector=None,
    *,
    include_self=True,
    import_packages=True,
    recursive=True,
    allow_magic=False,
    include_submodules=False,
    name_re=None,
    obj_type=None,
    )`

    * `package`, `include_self`, `import_packages`, `recursive`:
        See `PythonPackageImporter`.
        Please note that the default values for the flags are different from `PythonPackageImporter`.

    * `selector: typing.Callable[[str, typing.Any], bool] = None`:
        A callable accepting `(name, obj)` and returning a `bool`.
        Only variables that result in `True` will be included in the results.
        Ignored if `None`.
        Works in tandem with all other selectors below,
        i.e. only variables that match all criteria are included in the results.

    * `allow_magic: bool = False`:
        Allow variables with names starting with `__`.

    * `include_submodules: bool = False`:
        Allow submodule variables.
        In other words, whether variables of type `types.ModuleType` will be included in the results.

    * `name_re: re.Pattern = None`:
        A regex pattern that variable names need to match.
        Ignored if `None`.

    * `obj_type: typing.Union[typing.Type, typing.Tuple[typing.Type, ...]] = None`:
        A type or a tuple of types that variables need to match.
        `isinstance` will be used.

* `__iter__() -> typing.Iterator[typing.Tuple[str, str, typing.Any]]`

    Iterate through all matching variables in the package.
    Each result will be (module name, variable name, variable).

    Implicitly this will also import the modules containing the variables.

* `__call__() -> typing.List[typing.Tuple[str, str, typing.Any]]`

    Return a list of all matching variables found in the package.

    Implicitly this will also import the modules containing the variables.

Example:

```python
from python_package_importer.object_finder import PythonPackageObjectFinder
import my_package

finder = PythonPackageObjectFinder(
    my_package,
    obj_type=(int, float),
)
total = sum(v for _, _, v in finder)  # calculate sum for all int or float variables found in the package
```

### class `python_package_importer.pytest.PytestFixturePackageLoader`

Load all pytest fixtures defined in a package.

* `__init__(
    package,
    )`

    * `package`:
        See `PythonPackageImporter`.

    * Please note that `include_self` and `recursive` are set to `True`.

* `__call__(
    locals_,
    ) -> None`

    * `locals_: typing.Dict[str, typing.Any]`:
        A dictionary to accept the fixtures as variables.
        Most likely you will want to pass in `locals()`.

Example:

```python
# conftest.py
from python_package_importer.pytest import PytestFixturePackageLoader
from . import my_fixtures  # <--- A package containing a lot of fixtures

PytestFixturePackageLoader(my_fixtures)(locals())  # <--- Load all fixtures into conftest.py
```
