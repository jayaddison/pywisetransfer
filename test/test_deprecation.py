from warnings import catch_warnings

import pytest

from pywisetransfer.deprecation import deprecated

record_warnings = lambda: catch_warnings(record=True)


def undecorated(n):
    return n


@deprecated
def bare_decorator(n):
    return n + 1


@deprecated()
def zero_args_decorator(n):
    return n + 2


@deprecated("positional")
def posarg_decorator(n):
    return n + 3


@deprecated(message="keyword")
def kwarg_decorator(n):
    return n + 4


class Class:
    @deprecated(message="instance")
    def method(self, n):
        return n + 5


instancemethod_decorator = Class().method


@pytest.mark.parametrize(
    "func, name, deprecated, result, message",
    [
        (undecorated, "undecorated", False, 0, None),
        (bare_decorator, "bare_decorator", True, 1, None),
        (zero_args_decorator, "zero_args_decorator", True, 2, None),
        (posarg_decorator, "posarg_decorator", True, 3, "positional"),
        (kwarg_decorator, "kwarg_decorator", True, 4, "keyword"),
        (instancemethod_decorator, "instancemethod_decorator", True, 5, "instance"),
    ],
)
def test_decorator_variants(func, name, deprecated, result, message):
    actual_repr = repr(func)
    with record_warnings() as ws:
        actual_result = func(0)

    # Check the Python repr of the function
    assert name in actual_repr
    actual_deprecated = "deprecated" in actual_repr
    assert deprecated == actual_deprecated

    # Check the behaviour of the function
    assert result == actual_result

    # Check the warnings emitted by the function
    assert ws if deprecated else not ws
    assert any([message in str(w.message) for w in ws] if message else [True])
