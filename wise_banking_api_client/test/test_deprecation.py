from warnings import catch_warnings

import pytest

from wise_banking_api_client.deprecation import deprecated


def record_warnings():
    return catch_warnings(record=True)


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
    base = 2

    @deprecated(message="method")
    def method_decorator(self, n):
        return self.base + n + 3


@pytest.mark.parametrize(
    "func, name, deprecated, result, message",
    [
        (undecorated, "undecorated", False, 0, None),
        (bare_decorator, "bare_decorator", True, 1, None),
        (zero_args_decorator, "zero_args_decorator", True, 2, None),
        (posarg_decorator, "posarg_decorator", True, 3, "positional"),
        (kwarg_decorator, "kwarg_decorator", True, 4, "keyword"),
        (Class().method_decorator, "method_decorator", True, 5, "method"),
    ],
)
def test_decorator_variants(func, name, deprecated, result, message):
    actual_repr = repr(func)
    with record_warnings() as ws:
        actual_result = func(0)

    # Check the Python repr of the function
    assert name in actual_repr
    actual_deprecated = "deprecated." in actual_repr
    assert deprecated == actual_deprecated

    # Check the behaviour of the function
    assert result == actual_result

    # Check the warnings emitted by the function
    assert len(ws) == 1 if deprecated else not ws
    assert any([message in str(w.message) for w in ws] if message else [True])


def test_standalone_decorator_repr():
    decorator = deprecated(message="standalone")
    assert repr(decorator) == "<deprecation decorator ('standalone')>"
