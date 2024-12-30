"""Allow recoring and dumping of API information.

Use it like this:


"""
from pathlib import Path
from typing import Optional
from responses import _recorder

HERE = Path(__file__).parent
RESPONSES = HERE / "responses"


def record(name:Optional[str] = None) -> None:
    """Start recording requests to the API.
    
    If the name is None, we just stop recording.
    Otherwise, we save it.
    """
    if name is not None:
        _recorder.recorder.dump_to_file(
            RESPONSES / f"{name}.yaml", 
            _recorder.recorder.get_registry().registered)
    _recorder.recorder.reset()
    
__all__ = ["RESPONSES", "record"]
