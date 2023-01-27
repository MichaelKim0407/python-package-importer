# < 3.8
try:
    from functools import cached_property
except ImportError:  # pragma: no cover
    from cached_property import cached_property  # noqa: pycharm
