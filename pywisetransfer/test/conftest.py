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
import responses
from pywisetransfer.test.record import RESPONSES


@pytest.fixture
def sandbox() -> Generator[Client, None, None]:
    """We return a sandbox client and dispatch all requests.

    The responses are loaded from the RESPONSES directory.

    """
    rsps = responses.RequestsMock()
    rsps.start()
    # see https://github.com/getsentry/responses?tab=readme-ov-file#replay-responses-populate-registry-from-files
    for path in RESPONSES.iterdir():
        rsps._add_from_file(file_path=path)
    yield Client(api_key="test-key", environment="sandbox")
    rsps.stop(allow_assert=False)
