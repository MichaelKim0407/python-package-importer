import types
import typing

from .object_finder import PythonPackageObjectFinder


class PytestFixturePackageLoader:
    def __init__(
            self,
            package: types.ModuleType,
    ):
        self.object_finder = PythonPackageObjectFinder(
            package,
            self._is_fixture,
            include_self=True,
            recursive=True,
        )

    _FUNCTION_FLAG = '_pytestfixturefunction'

    @classmethod
    def _is_fixture(cls, name: str, obj) -> bool:
        return hasattr(obj, cls._FUNCTION_FLAG)

    def __call__(self, locals_: typing.Dict[str, typing.Any]) -> None:
        for module_name, name, obj in self.object_finder:
            locals_[name] = obj
