"""The timestamp of a model.

See https://stackoverflow.com/a/77543303/1320237
"""

from typing_extensions import Annotated
from datetime import datetime, timezone
from pydantic import PlainSerializer, BeforeValidator

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def parse_timestamp(s: str) -> datetime:
    """Parse a timestamp as Wise specifies it."""
    return datetime.strptime(s, DATETIME_FORMAT).replace(tzinfo=timezone.utc)


def serialize_timestamp(dt: datetime) -> str:
    """Serialize a timestamp as Wise uses it."""
    return dt.strftime(DATETIME_FORMAT)


Timestamp = Annotated[
    datetime,
    BeforeValidator(parse_timestamp),
    PlainSerializer(serialize_timestamp),
]

__all__ = ["Timestamp", "DATETIME_FORMAT", "parse_timestamp", "serialize_timestamp"]
