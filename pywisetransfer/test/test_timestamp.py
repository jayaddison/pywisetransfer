"""Test timespam parsing."""

from datetime import datetime, timezone

from pywisetransfer.model.timestamp import DATETIME_FORMAT, parse_timestamp, serialize_timestamp


def test_parse_example_stamp():
    """Parse a stamp from the example."""
    datetime.strptime("2019-04-08T12:30:00Z", DATETIME_FORMAT)


def test_parse_unparse_is_the_same():
    """Check the values do not change."""
    s = "2019-04-08T10:30:00Z"
    assert serialize_timestamp(parse_timestamp(s)) == s


def test_value():
    """Test the value of the parsed object."""
    dt = parse_timestamp("2019-04-08T10:30:01Z")
    assert dt == datetime(2019, 4, 8, 10, 30, 1, tzinfo=timezone.utc)
