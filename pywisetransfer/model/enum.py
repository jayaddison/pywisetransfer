"""Enums for the API."""

from enum import Enum


class StrEnum(str, Enum):
    """An enum which can be serialized and validated."""

    def __repr__(self) -> str:
        """Return only the value of the enum."""
        return repr(self.value)

    def __str__(self) -> str:
        """Return only the value of the enum."""
        return self.value


__all__ = ["StrEnum"]
