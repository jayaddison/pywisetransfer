"""The timestamp of a model.

See https://stackoverflow.com/a/77543303/1320237
"""

from typing import Optional
from typing_extensions import Annotated
from datetime import date, datetime, timezone
from pydantic import PlainSerializer, BeforeValidator

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def parse_timestamp(s: str | None) -> Optional[datetime]:
    """Parse a timestamp as Wise specifies it.

    If None is returned, None is the result.
    """
    if s is None:
        return None
    if s[-1] != "Z":
        s += "Z"  # compatibility with older API calls
    if " " in s:
        s = s.replace(" ", "T")
    return datetime.strptime(s, DATETIME_FORMAT).replace(tzinfo=timezone.utc)


def serialize_timestamp(dt: datetime) -> str:
    """Serialize a timestamp as Wise uses it."""
    return dt.strftime(DATETIME_FORMAT)


Timestamp = Annotated[
    datetime,
    BeforeValidator(parse_timestamp),
    PlainSerializer(serialize_timestamp),
]


def parse_date(s: str) -> date:
    """Parse a timestamp as Wise specifies it."""
    return date(*map(lambda x: int(x.lstrip("0")), s.split("-")))


def serialize_date(dt: date) -> str:
    """Serialize a timestamp as Wise uses it."""
    return f"{dt.year}-{dt.month:02d}-{dt.day:02d}"


Date = Annotated[
    date,
    BeforeValidator(parse_date),
    PlainSerializer(serialize_date),
]

OptionalDate = Annotated[
    Optional[date],
    BeforeValidator(lambda x: None if x is None else parse_date(x)),
    PlainSerializer(lambda x: None if x is None else serialize_date(x)),
]


__all__ = [
    "Timestamp",
    "DATETIME_FORMAT",
    "parse_timestamp",
    "serialize_timestamp",
    "Date",
    "OptionalDate",
]
