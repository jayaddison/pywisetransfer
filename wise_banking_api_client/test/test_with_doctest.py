"""This file tests the source code provided by the documentation.

See
- doctest documentation: https://docs.python.org/3/library/doctest.html
- Issue 443: https://github.com/collective/icalendar/issues/443

This file should be tests, too:

    >>> print("Hello World!")
    Hello World!

"""

import doctest
import importlib
import pathlib
import sys

import pytest

HERE = pathlib.Path(__file__).parent
PROJECT_PATH = HERE.parent

PYTHON_FILES = list(PROJECT_PATH.rglob("*.py"))

MODULE_NAMES = [
    "wise_banking_api_client",
]


@pytest.mark.parametrize("module_name", MODULE_NAMES)
def test_docstring_of_python_file(module_name):
    """This test runs doctest on the Python module."""
    module = importlib.import_module(module_name)
    test_result = doctest.testmod(module, name=module_name)
    assert test_result.failed == 0, f"{test_result.failed} errors in {module_name}"


# This collection needs to exclude .tox and other subdirectories
DOCUMENT_PATHS = [PROJECT_PATH / ".." / "README.md"] + PYTHON_FILES


def test_this_file_is_also_tested():
    """Check we recurse."""
    paths = list(map(str, DOCUMENT_PATHS))
    print("Documents:\n", "\n".join(paths))
    assert __file__ in paths


def doctest_print(obj=""):
    """doctest print"""
    if isinstance(obj, bytes):
        obj = obj.decode("UTF-8")
    print(str(obj).rstrip().replace("\r\n", "\n").replace("\r", "\n"))


@pytest.mark.parametrize("document", DOCUMENT_PATHS)
def test_documentation_file(document):
    """This test runs doctest on a documentation file.

    functions are also replaced to work.
    """
    test_result = doctest.testfile(
        str(document),
        module_relative=False,
        globs={"print": doctest_print},
        raise_on_error=False,
    )
    assert test_result.failed == 0, f"{test_result.failed} errors in {document.name}"
