from .enum import StrEnum


class ProfileType(StrEnum):
    """The type of profile."""

    PERSONAL = "PERSONAL"
    BUSINESS = "BUSINESS"


__all__ = ["ProfileType"]
