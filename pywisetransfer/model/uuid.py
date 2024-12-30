"""This is a simple way to generate UUIDs.

"""

import uuid
from pydantic import Field

# see https://stackoverflow.com/a/18516125/1320237 for regex
UUID_REGEX = "[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}"

# see https://stackoverflow.com/a/74613586/1320237 for Field
UUID = Field(pattern=UUID_REGEX)


def new_uuid() -> str:
    """Create a new UUID as expected by Wise.

    See https://docs.python.org/3/library/uuid.html
    """
    return str(uuid.uuid4())


__all__ = ["UUID_REGEX", "UUID", "new_uuid"]
