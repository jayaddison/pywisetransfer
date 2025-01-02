"""pytest configuration

You can add responses by running this in your codebase:

    from pywisetransfer.test import record

    record()
    # do API requests
    record("name-of-endpoint")

"""

from typing import Generator
import pytest
from pywisetransfer import Client
from pywisetransfer.test.record import TestClient
from pywisetransfer.model.currency import Currency


@pytest.fixture(scope="package")
def sandbox() -> Generator[Client, None, None]:
    """We return a sandbox client and dispatch all requests.

    The responses are loaded from the RESPONSES directory.

    """
    client = TestClient()
    yield client
    client.stop()

@pytest.fixture(params=Currency.all_currencies())
def currency(request):
    return request.param