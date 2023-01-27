import typing

# < 3.8
try:
    from functools import cached_property
except ImportError:  # pragma: no cover
    from cached_property import cached_property  # noqa: pycharm

# < 3.10
try:
    TypeAlias = typing.TypeAlias
except AttributeError:  # pragma: no cover
    TypeAlias = typing.Any
