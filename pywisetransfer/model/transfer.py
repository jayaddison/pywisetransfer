"""The model classes for transfers."""

from __future__ import annotations
from datetime import date
from uuid import UUID

from pydantic import Field, PlainSerializer

from pywisetransfer.model.legal_type import LegalType
from pywisetransfer.model.account import LegalEntityType, RecipientName
from pywisetransfer.model.annotations import WithoutNone
from pywisetransfer.model.currency import CURRENCY
from pywisetransfer.model.recipient.address import AddressDetails
from pywisetransfer.model.timestamp import Timestamp
from pywisetransfer.model.uuid import new_uuid
from .enum import StrEnum
from typing import Annotated, ClassVar, Optional
from .base import BaseModel


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
    waiting_recipient_input_to_proceed = "waiting_recipient_input_to_proceed"

    @property
    def description(self) -> str:
        """The description of the transfer status."""
        return TransferStatusDescription[self]

    transfer_simulation: list[TransferStatus]


TransferStatus.transfer_simulation = [
    TransferStatus.processing,
    TransferStatus.funds_converted,
    TransferStatus.outgoing_payment_sent,
    TransferStatus.bounced_back,
    TransferStatus.funds_refunded,
]


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
    TransferStatus.waiting_recipient_input_to_proceed: "Sent email to recipient",
}


class TransferDetails(BaseModel):
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
    transferPurpose: Optional[str] = None
    transferPurposeSubTransferPurpose: Optional[str] = None
    sourceOfFunds: Optional[str] = None


class TransferRequest(BaseModel):
    """A transfer object to create transfers on Wise.

    See https://docs.wise.com/api-docs/api-reference/transfer#create

    Attributes:

        sourceAccount: Refund recipient account ID
        targetAccount: Recipient account ID. You can create multiple transfers to same recipient account.
        quoteUuid: V2 quote ID. You can only create one transfer per one quote. You cannot use same quote ID to create multiple transfers.
        customerTransactionId: This is required to perform idempotency check to avoid duplicate transfers in case of network failures or timeouts.
        details: Transfer details
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "sourceAccount": 100000,
        "targetAccount": 100001,
        "quoteUuid": "00000000-0000-0000-0000-000000000000",
        "customerTransactionId": "11111111-1111-1111-1111-111111111111",
        "details": {
            "reference": "to my friend",
            "transferPurpose": "verification.transfers.purpose.pay.bills",
            "transferPurposeSubTransferPurpose": "verification.sub.transfers.purpose.pay.interpretation.service",
            "sourceOfFunds": "verification.source.of.funds.other"
        }
    }
    """

    sourceAccount: Optional[int] = None
    targetAccount: int
    quoteUuid: Annotated[UUID, PlainSerializer(str)]
    customerTransactionId: Annotated[UUID, PlainSerializer(str)] = Field(default_factory=new_uuid)
    details: TransferDetails


class OriginatorGroup(BaseModel):
    """Data block to capture payment originator details.

    Attributes:
        legalEntityType: Legal entity type
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "legalEntityType": "PRIVATE",
        "name": {
            "fullName": "John Godspeed",
            "givenName": "John",
            "familyName": "Godspeed"
        },
        "reference": "CST-2991992",
        "dateOfBirth": "1977-07-01",
        "businessRegistrationCode": null,
        "address": {
            "countryCode": "EE",
            "city": "Tallinn",
            "firstLine": "Salu tee 14",
            "postCode": "12112"
        }
    }
    """

    legalEntityType: LegalEntityType | LegalType
    name: Optional[WithoutNone[RecipientName]] = None
    reference: Optional[str] = None
    dateOfBirth: Optional[date] = None
    businessRegistrationCode: Optional[str] = None
    address: Optional[WithoutNone[AddressDetails]] = None


class TransferResponse(BaseModel):
    """A response from a created transfer.

    See https://docs.wise.com/api-docs/api-reference/transfer#object

    Attributes:
        id: Transfer ID
        user: Your User ID
        targetAccount: Recipient account ID
        sourceAccount: Refund recipient account ID
        quote: v1 quote ID (where applicable)
        quoteUuid: v2 quote ID
        status: Transfer status
        rate: Exchange rate value
        created: Date and time when the transfer was created
        business: Business ID of the source profile
        details: Transfer details
        hasActiveIssues: Are there any pending issues which stop executing the transfer?
        sourceCurrency: Source (sending) currency code.
        targetCurrency: Target (receiving) currency code.
        sourceValue: Source (sending) amount.
        targetValue: Target (receiving) amount.
        customerTransactionId: Unique identifier randomly generated per transfer request by the calling client
        originator: Data block to capture payment originator details
    """

    id: int
    user: int
    targetAccount: int
    sourceAccount: Optional[int] = None
    quote: Optional[int] = None
    quoteUuid: Optional[UUID] = None
    status: TransferStatus
    reference: Optional[str] = Field(deprecated=True, alias="details.reference", default=None)
    rate: float
    created: Timestamp
    business: Optional[int]
    transferRequest: Optional[int] = Field(deprecated=True, default=None)
    details: TransferDetails
    hasActiveIssues: bool
    sourceCurrency: str = CURRENCY
    sourceValue: float | int
    targetCurrency: str = CURRENCY
    targetValue: float | int
    customerTransactionId: UUID
    originator: Optional[WithoutNone[OriginatorGroup]] = None


__all__ = [
    "TransferRequest",
    "TransferResponse",
    "TransferDetails",
    "TransferStatus",
    "TransferStatusDescription",
    "OriginatorGroup",
]
