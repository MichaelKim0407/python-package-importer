# < 3.8
try:
    from functools import cached_property
except ImportError:  # pragma: no cover
    from cached_property import cached_property  # noqa: pycharm

# < 3.10
try:
    from typing import TypeAlias
except ImportError:  # pragma: no cover
    from typing import Any as TypeAlias  # noqa: F401
