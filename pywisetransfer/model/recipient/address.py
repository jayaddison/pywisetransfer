# generated file
#    python -m pywisetransfer.model.recipient && black .

from pydantic import BaseModel, Field
from typing import Optional, ClassVar
from .literals import ADDRESS_COUNTRY


class AddressDetails(BaseModel):
    """The address details of a transfer or recipient.

    Attributes:
        firstLine: address first line
        city: address city
        stateCode: address state code
        countryCode: address country code
        postCode: address zip code
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "firstLine": "Salu tee 14",
        "city": "Tallinn",
        "stateCode": null,
        "countryCode": "EE",
        "postCode": "12112"
    }
    """

    stateCode: Optional[str] = None
    countryCode: Optional[ADDRESS_COUNTRY] = None

    @property
    def country_code(self) -> ADDRESS_COUNTRY:
        """The country code."""
        return self.countryCode or self.country

    city: Optional[str] = Field(
        examples=None, min_length=1, max_length=255, pattern="(^.{1,255}$)", default=None
    )
    firstLine: Optional[str] = Field(
        examples=None, min_length=1, max_length=255, pattern="(^.{1,255}$)", default=None
    )
    postCode: Optional[str] = Field(
        examples=None, min_length=1, max_length=32, pattern="(^.{1,32}$)", default=None
    )
    country: Optional[ADDRESS_COUNTRY] = None


__all__ = ["AddressDetails"]
