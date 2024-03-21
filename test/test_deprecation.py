from warnings import catch_warnings

import pytest

from pywisetransfer.deprecation import deprecated

record_warnings = lambda: catch_warnings(record=True)


def undecorated():
    return 1


@deprecated
def bare_decorator():
    return 1


@deprecated()
def zero_args_decorator():
    return 1


@deprecated("positional")
def posarg_decorator():
    return 1


@deprecated(message="keyword")
def kwarg_decorator():
    return 1


@pytest.mark.parametrize(
    "func, name, deprecated, message",
    [
        (undecorated, "undecorated", False, None),
        (bare_decorator, "bare_decorator", True, None),
        (zero_args_decorator, "zero_args_decorator", True, None),
        (posarg_decorator, "posarg_decorator", True, "positional"),
        (kwarg_decorator, "kwarg_decorator", True, "keyword"),
    ],
)
def test_no_decorator(func, name, deprecated, message):
    actual_repr = repr(func)
    with record_warnings() as ws:
        result = func()

    # Check the Python repr of the function
    assert name in actual_repr
    actual_deprecated = "deprecated" in actual_repr
    assert deprecated == actual_deprecated

    # Check the behaviour of the function
    assert result == 1

    # Check the warnings emitted by the function
    assert ws if deprecated else not ws
    assert any([message in str(w.message) for w in ws] if message else [True])
