"""Country models."""

from pydantic import Field

COUNTRY_CODE_REGEX = "[A-Za-z][A-Za-z]"

COUNTRY_CODE = Field(
    title="country",
    description="2 character country code",
    examples=["GB", "US"],
    pattern=COUNTRY_CODE_REGEX,
)

__all__ = [
    "COUNTRY_CODE",
]
