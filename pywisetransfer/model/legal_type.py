from pywisetransfer.model.enum import StrEnum


class LegalType(StrEnum):
    """The legal type of a recipient account."""

    PRIVATE = "PRIVATE"
    BUSINESS = "BUSINESS"
    
__all__ = ["LegalType"]
