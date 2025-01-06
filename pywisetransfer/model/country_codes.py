from pywisetransfer.model.enum import StrEnum
from .recipient.literals import ADDRESS_COUNTRY_VALUES

# see https://stackoverflow.com/a/33690233/1320237
Country = StrEnum("Country", {code: code for code in ADDRESS_COUNTRY_VALUES})

__all__ = ["Country"]
