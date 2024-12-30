"""The timestamp of a model.

See https://stackoverflow.com/a/77543303/1320237
"""

from typing_extensions import Annotated
from datetime import datetime, timezone
from pydantic import PlainSerializer, BeforeValidator


Timestamp = Annotated[
    datetime,
    BeforeValidator(lambda s: datetime.strptime(s, '%Y-%m-%dT%H:%M%Z').astimezone(tz=timezone.utc)),
    PlainSerializer(lambda dt: dt.strftime('%Y-%m-%dT%H:%M:%SZ'))
]

__all__ = ["Timestamp"]
