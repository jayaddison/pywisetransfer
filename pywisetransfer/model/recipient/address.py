# generated file
#    python -m pywisetransfer.model.recipient && black .

from pydantic import BaseModel, Field
from typing import Optional
from .literals import ADDRESS_COUNTRY


class AddressDetails(BaseModel):

    city: Optional[str] = Field(min_length=1, max_length=255, pattern="^.{1,255}$", default=None)
    firstLine: Optional[str] = Field(
        min_length=1, max_length=255, pattern="^.{1,255}$", default=None
    )
    postCode: Optional[str] = Field(min_length=1, max_length=32, pattern="^.{1,32}$", default=None)
    country: Optional[ADDRESS_COUNTRY] = None


__all__ = ["AddressDetails"]
