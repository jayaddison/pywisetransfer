from warnings import catch_warnings

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


@deprecated("test message")
def posarg_decorator():
    return 1


@deprecated(message="test message")
def kwarg_decorator():
    return 1


def test_no_decorator():
    actual_repr = repr(undecorated)
    with record_warnings() as ws:
        result = undecorated()

    assert "deprecated" not in actual_repr
    assert result == 1
    assert not ws


def test_decorator_bare():
    actual_repr = repr(bare_decorator)
    with record_warnings() as ws:
        result = bare_decorator()

    assert "deprecated" in actual_repr
    assert "function bare_decorator" in actual_repr
    assert result == 1
    assert ws


def test_decorator_zero_args():
    actual_repr = repr(zero_args_decorator)
    with record_warnings() as ws:
        result = zero_args_decorator()

    assert "deprecated" in actual_repr
    assert "function zero_args_decorator" in actual_repr
    assert result == 1
    assert ws


def test_decorator_with_args():
    actual_repr = repr(posarg_decorator)
    with record_warnings() as ws:
        result = posarg_decorator()

    assert "deprecated" in actual_repr
    assert "function posarg_decorator" in actual_repr
    assert result == 1
    assert ws
    assert any([str(w.message) == "test message" for w in ws])


def test_decorator_with_kwargs():
    actual_repr = repr(kwarg_decorator)
    with record_warnings() as ws:
        result = kwarg_decorator()

    assert "deprecated" in actual_repr
    assert "function kwarg_decorator" in actual_repr
    assert result == 1
    assert ws
    assert any([str(w.message) == "test message" for w in ws])
