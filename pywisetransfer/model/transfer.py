"""The model classes for transfers."""

from .enum import StrEnum
from typing import ClassVar, Optional
from pydantic import BaseModel


class TransferStatus(StrEnum):
    """The transfer status

    See https://docs.wise.com/api-docs/guides/send-money/tracking

    You can use TransferStatusDescription to indicate the transfer status
    to the user.
    """

    incoming_payment_waiting = "incoming_payment_waiting"
    incoming_payment_initiated = "incoming_payment_initiated"
    processing = "processing"
    funds_converted = "funds_converted"
    outgoing_payment_sent = "outgoing_payment_sent"
    cancelled = "cancelled"
    funds_refunded = "funds_refunded"
    bounced_back = "bounced_back"
    charged_back = "charged_back"
    unknown = "unknown"


TransferStatusDescription = {
    TransferStatus.incoming_payment_waiting: "On its way to Wise",
    TransferStatus.incoming_payment_initiated: "On its way to Wise",
    TransferStatus.processing: "Processing",
    TransferStatus.funds_converted: "Processing",
    TransferStatus.outgoing_payment_sent: "Sent",
    TransferStatus.cancelled: "Cancelled",
    TransferStatus.funds_refunded: "Refunded",
    TransferStatus.bounced_back: "Bounced back",
    TransferStatus.charged_back: "Charged back",
    TransferStatus.unknown: "Unknown",
}


class Details(BaseModel):
    """The details of a transfer.

    See https://docs.wise.com/api-docs/api-reference/transfer#create

    Attributes:
        reference: Recipient will see this reference text in their bank statement.
            Maximum allowed characters depends on the currency route.
            Business Payments Tips article has a full list.
            https://wise.com/help/articles/2932870/tips-for-paying-invoices
        transferPurpose: For example when target currency is THB.
            See more about conditions at Transfers.Requirements:
            https://docs.wise.com/api-docs/api-reference/transfer#transfer-requirements
        transferPurposeSubTransferPurpose: For example when target currency is CNY.
            See more about conditions at Transfers.Requirements:
            https://docs.wise.com/api-docs/api-reference/transfer#transfer-requirements
        sourceOfFunds: For example when target currency is USD and transfer amount exceeds 80k.
            See more about conditions at Transfers.Requirements:
            https://docs.wise.com/api-docs/api-reference/transfer#transfer-requirements

    There are two options to deal with conditionally required fields:

    - Always call transfer-requirements endpoint and submit values only if indicated so.
    - Always provide values for these fields based on a dynamically retrieved list
        (transfer-requirements endpoint).
        It is possible these fields change over time so hard coding the options does create some risk of issues.
        Contact api@wise.com if you have questions about this property,
        especially if considering hardcoding a value.
    """

    reference: str
    transferPurpose: Optional[str]
    transferPurposeSubTransferPurpose: Optional[str]
    sourceOfFunds: Optional[str]


class Transfer(BaseModel):
    """A transfer object to create transfers on Wise.

    See https://docs.wise.com/api-docs/api-reference/transfer#create

    Attributes:

        sourceAccount: Refund recipient account ID
        targetAccount: Recipient account ID. You can create multiple transfers to same recipient account.
        quoteUuid: V2 quote ID. You can only create one transfer per one quote. You cannot use same quote ID to create multiple transfers.
        customerTransactionId: This is required to perform idempotency check to avoid duplicate transfers in case of network failures or timeouts.
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """{
        "sourceAccount": <refund recipient account ID>,
        "targetAccount": <recipient account ID>,
        "quoteUuid": <quote ID>,
        "customerTransactionId": "<the unique identifier you generated for the transfer attempt>",
        "details" : {
            "reference" : "to my friend",
            "transferPurpose": "verification.transfers.purpose.pay.bills",
            "transferPurposeSubTransferPurpose": "verification.sub.transfers.purpose.pay.interpretation.service"
            "sourceOfFunds": "verification.source.of.funds.other"
        }
    }
    """

    sourceAccount: int
    targetAccount: int
    quoteUuid: str
    customerTransactionId: str
    details: Details


__all__ = ["Transfer", "Details", "TransferStatus", "TransferStatusDescription"]
