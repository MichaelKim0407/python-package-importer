import re
import types
import typing

from returns import returns

from ._compatibility import cached_property, TypeAlias
from .importer import PythonPackageImporter

Selector: TypeAlias = typing.Callable[[str, typing.Any], bool]
Entry: TypeAlias = typing.Tuple[str, str, typing.Any]
Types: TypeAlias = typing.Union[typing.Type, typing.Tuple[typing.Type, ...]]


class PythonPackageObjectFinder:
    def __init__(
            self,
            package: types.ModuleType,
            selector: Selector = None,
            *,
            include_self: bool = True,
            import_packages: bool = True,
            recursive: bool = True,
            allow_magic: bool = False,
            include_submodules: bool = False,
            name_re: re.Pattern = None,
            obj_type: Types = None,
    ):
        self.importer = PythonPackageImporter(
            package,
            include_self=include_self,
            import_packages=import_packages,
            recursive=recursive,
        )
        self._selector = selector
        self.allow_magic = allow_magic
        self.include_submodules = include_submodules
        self.name_re = name_re
        self.obj_type = obj_type

    @cached_property
    @returns(list)
    def _selectors(self) -> typing.List[Selector]:
        if not self.allow_magic:
            yield lambda name, obj: not name.startswith('__')
        if not self.include_submodules:
            yield lambda name, obj: not isinstance(obj, types.ModuleType)
        if self.name_re is not None:
            yield lambda name, obj: self.name_re.fullmatch(name) is not None
        if self.obj_type is not None:
            yield lambda name, obj: isinstance(obj, self.obj_type)
        if self._selector is not None:
            yield self._selector

    def selector(self, name: str, obj) -> bool:
        for selector in self._selectors:
            if not selector(name, obj):
                return False
        return True

    def __iter__(self) -> typing.Iterator[Entry]:
        for module in self.importer:
            for name in dir(module):
                obj = getattr(module, name)
                if not self.selector(name, obj):
                    continue
                yield module.__name__, name, obj

    def __call__(self) -> typing.List[Entry]:
        return list(self)
