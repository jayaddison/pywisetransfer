from warnings import catch_warnings

from pywisetransfer.deprecation import deprecated


record_warnings = lambda: catch_warnings(record=True)


def test_no_decorator():
    def foo():
        return 1

    with record_warnings() as ws:
        result = foo()

    assert result == 1
    assert not ws


def test_decorator_bare():
    @deprecated
    def foo():
        return 1

    with record_warnings() as ws:
        result = foo()

    assert result == 1
    assert ws


def test_decorator_zero_args():
    @deprecated()
    def foo():
        return 1

    with record_warnings() as ws:
        result = foo()

    assert result == 1
    assert ws


def test_decorator_with_args():
    @deprecated("test message")
    def foo():
        return 1

    with record_warnings() as ws:
        result = foo()

    assert result == 1
    assert ws
    assert any([str(w.message) == "test message" for w in ws])


def test_decorator_with_kwargs():
    @deprecated(message="test message")
    def foo():
        return 1

    with record_warnings() as ws:
        result = foo()

    assert result == 1
    assert ws
    assert any([str(w.message) == "test message" for w in ws])
