from __future__ import annotations

from typing import Any, Callable, Literal, TypeVar  # noqa: UP035

# https://mypy.readthedocs.io/en/stable/generics.html#decorator-factories
DecoratedCallable = TypeVar('DecoratedCallable', bound=Callable[..., Any])

_Type = Literal['send', 'receive']
