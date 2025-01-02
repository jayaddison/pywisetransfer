"""Allow recoring and dumping of API information.

Use it like this:


"""

from pathlib import Path
from typing import Optional
from pywisetransfer.client import Client

HERE = Path(__file__).parent
RESPONSES = HERE / "responses"

ERROR_MESSAGE = f"You need to install {__name__.split('.')[0]}[dev]."


def record(name: Optional[str] = None) -> None:
    """Start recording requests to the API.

    If the name is None, we just stop recording.
    Otherwise, we save it.
    """
    try:
        from responses import _recorder
    except ImportError:
        raise ImportError(ERROR_MESSAGE)
    if name is not None:
        file_name = RESPONSES / f"{name}.yaml"
        i = 0
        while file_name.exists():
            i += 1
            file_name = RESPONSES / f"{name}-{i}.yaml"
        _recorder.recorder.dump_to_file(
            file_path=file_name, registered=_recorder.recorder.get_registry().registered
        )
        file_name.write_text(file_name.read_text().replace("content-encoding: gzip", ""))
        print(f"recorded to {file_name}")
    _recorder.recorder.stop()
    _recorder.recorder.reset()
    _recorder.recorder.start()


class TestClient(Client):
    """A test client that uses the recorded API.

    You will not be able to create another client that
    uses the Wise API after this except if you do this:

    client.stop()
    """

    def __init__(self, api_key: str = "test-key"):
        super().__init__(api_key=api_key, environment="sandbox")
        try:
            from responses import RequestsMock
        except ImportError:
            raise ImportError(ERROR_MESSAGE)
        self.rsps = RequestsMock()
        self.rsps.start()
        # see https://github.com/getsentry/responses?tab=readme-ov-file#replay-responses-populate-registry-from-files
        for path in RESPONSES.iterdir():
            self.rsps._add_from_file(file_path=path)

    def stop(self):
        """Stop using the test API."""
        self.rsps.stop(allow_assert=False)


__all__ = ["RESPONSES", "record", "TestClient"]
