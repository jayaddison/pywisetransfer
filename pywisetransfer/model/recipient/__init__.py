"""Model for recipients of transfers.

See https://docs.wise.com/api-docs/api-reference/recipient
"""

from typing import Optional
from pywisetransfer.model.account import RequirementType
from pywisetransfer.model.base import BaseModel
from pywisetransfer.model.currency import CURRENCY
from .details import RecipientDetails
from .address import AddressDetails
from .literals import LANGUAGE


class EmailDetails(RecipientDetails):
    """Details for an email recipient.

    Attributes:
        email: Email address
    """

    email: str
    language: Optional[LANGUAGE] = None


class Recipient(BaseModel):
    """The recipient model.

    See https://docs.wise.com/api-docs/api-reference/recipient

    Please note that the recipient information is subject to requirements of a quote.

    Attributes:
        currency: 3 character currency code
        type: Recipient type
        profile: Personal or business profile ID.
            It is highly advised to pass the business profile ID in this field if your business account
            is managed by multiple users, so that the recipient can be accessed by all users authorized
            on the business account.
        accountHolderName: Recipient full name.
            This is subject to the requirements of a quote.
        ownedByCustomer: Whether this account is owned by the sending user
        details: Currency specific fields
            These are subject to the requirements of a quote.
    """

    currency: str = CURRENCY
    type: RequirementType
    profile: int
    accountHolderName: str
    ownedByCustomer: bool
    details: dict


__all__ = ["RecipientDetails", "Recipient", "EmailDetails", "AddressDetails"]