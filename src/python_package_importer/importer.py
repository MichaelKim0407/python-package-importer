import importlib
import os
import types
import typing

from ._compatibility import cached_property


class PythonPackageImporter:
    def __init__(
            self,
            package: types.ModuleType,
            *,
            include_self: bool = False,
            import_packages: bool = False,
            recursive: bool = False,
    ):
        self.package = package
        self.include_self = include_self
        self.import_packages = import_packages or recursive
        self.recursive = recursive

    @cached_property
    def path(self) -> str:
        return os.path.dirname(self.package.__file__)

    @cached_property
    def package_name(self):
        return self.package.__name__

    def _isfile(self, *filename: str) -> bool:
        return os.path.isfile(os.path.join(self.path, *filename))

    def _isdir(self, *dirname: str) -> bool:
        return os.path.isdir(os.path.join(self.path, *dirname))

    def _import_module(self, name: str) -> types.ModuleType:
        return importlib.import_module(f'{self.package_name}.{name}')

    def _handle_dir(self, dirname: str) -> typing.Iterator[types.ModuleType]:
        if not self._isfile(dirname, '__init__.py'):
            return
        if not self.import_packages:
            return
        package = self._import_module(dirname)
        yield package
        if self.recursive:
            yield from self._recursive(package)

    def _recursive(self, package: types.ModuleType) -> typing.Iterator[types.ModuleType]:
        yield from PythonPackageImporter(
            package,
            include_self=False,
            recursive=True,
            import_packages=True,
        )

    def _handle_file(self, filename: str) -> typing.Iterator[types.ModuleType]:
        if not filename.endswith('.py'):
            return

        if filename == '__init__.py':
            return

        yield self._import_module(filename[:-3])

    def __iter__(self) -> typing.Iterator[types.ModuleType]:
        if self.include_self:
            yield self.package

        for filename in os.listdir(self.path):
            if self._isdir(filename):
                yield from self._handle_dir(filename)
            elif self._isfile(filename):
                yield from self._handle_file(filename)

    def __call__(self) -> typing.List[types.ModuleType]:
        return list(self)
