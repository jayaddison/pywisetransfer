"""The currency model."""

from pydantic import BaseModel, Field


CODE_REGEX = "[A-Z][A-Z][A-Z]"
CURRENCY = Field(
    title="code",
    description="Currency code (ISO 4217 Alphabetic Code)",
    examples=["USD", "EUR"],
    pattern=CODE_REGEX,
)


class Currency(BaseModel):
    """The currency model.

    See https://docs.wise.com/api-docs/api-reference/currencies

    Attributes:
        code: Currency code (ISO 4217 Alphabetic Code)
        symbol: The symbol of this currency
        name: Display name of this currency
        countryKeywords: Keywords associated with this currency
        supportsDecimals: Whether this currency supports decimal values or not
    """

    code: str = CURRENCY
    symbol: str
    name: str
    countryKeywords: list[str]
    supportsDecimals: bool


__all__ = ["Currency", "CURRENCY"]
