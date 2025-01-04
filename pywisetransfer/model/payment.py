"""Models for funding a transfer."""

from typing import ClassVar, Literal, Optional
from pywisetransfer.model.base import BaseModel
from pywisetransfer.model.enum import StrEnum


class PaymentType(StrEnum):
    """Payment typy of a transfer.
    There is currently one type of funding that can be completed:

    Attributes:
        BALANCE: Funds are pulled from a multi-currency account held with Wise.

    If funding from BALANCE, and your multi-currency account does not have the required
    funds to complete the action, then this call will fail with an "insufficient funds"
    error. Once funds are added and available, you must call this endpoint again.
    """

    BALANCE = "BALANCE"


class Payment(BaseModel):
    """How to pay a transfer.

    Attributes:
        type: Payment type (BALANCE)
        partnerReference: The transaction/payment identifier in your system, uniquely
            identifies the transfer in your platform.
            This is required for the Cross Currency Bulk Settlement model.
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "type": "BALANCE"
    }
    """

    type: PaymentType = PaymentType.BALANCE


class PaymentStatus(StrEnum):
    """The status of a payment."""

    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"


ERROR_CODE = Literal["balance.payment-option-unavailable", "transfer.insufficient_funds"]


class PaymentResponse(BaseModel):
    """Response from a completed payment."""

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "type": "BALANCE",
        "status": "COMPLETED",
        "errorCode": null
    }
    """

    type: PaymentType = PaymentType.BALANCE
    status: PaymentStatus = PaymentStatus.COMPLETED
    errorCode: Optional[ERROR_CODE | str] = None


__all__ = ["Payment", "PaymentType", "PaymentResponse", "PaymentStatus"]
