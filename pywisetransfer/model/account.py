"""The account models.


See https://docs.wise.com/api-docs/api-reference/recipient

"""

from datetime import date
from typing import Annotated, ClassVar, Optional

from pydantic import BeforeValidator, Field
from pywisetransfer.model.annotations import WithoutNone
from pywisetransfer.model.base import DOCUMENTED_BUT_ABSENT, BaseModel
from pywisetransfer.model.country import COUNTRY_CODE
from pywisetransfer.model.currency import CURRENCY
from pywisetransfer.model.enum import StrEnum
from pywisetransfer.model.profile import PROFILE_TYPE
from pywisetransfer.model.recipient.details import (
    RecipientDetails as RecipientAccountRequestDetails,
)
from pywisetransfer.model.account_requirement_type import AccountRequirementType
from pywisetransfer.model.requirements import (
    AccountRequirement,
    RequiredField,
    RequirementsList,
)


class RecipientName(BaseModel):
    """The recipient name.

    Attributes:
        fullName: Recipient full name
        givenName: Recipient first name
        familyName: Recipient surname
        middleName: Recipient middle name
        patronymicName: The patronymic name of the recipient.
        cannotHavePatronymicName: The patronymic name of the recipient.
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "fullName": "John Doe",
        "givenName": null,
        "familyName": null,
        "middleName": null,
        "patronymicName": null,
        "cannotHavePatronymicName": null
    }
    """
    fullName: str
    givenName: Optional[str] = None
    familyName: Optional[str] = None
    middleName: Optional[str] = None
    patronymicName: Optional[str] = None
    cannotHavePatronymicName: object = None


class CommonFieldMap(BaseModel):
    """Map of key lookup fields on the account.

    Attributes:
        bankCodeField: Bank sort code identifier field
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "accountNumberField": "accountNumber",
        "bankCodeField": "sortCode"
    }
    """
    accountNumberField: Optional[str] = None
    bankCodeField: Optional[str] = None


class DisplayField(BaseModel):
    """Lookup fields."""

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "key": "details/sortCode",
        "label": "UK sort code",
        "value": "04-00-75"
    }
    """

    key: str
    label: str
    value: str


class LegalType(StrEnum):
    """The legal type of a recipient account."""

    PRIVATE = "PRIVATE"
    BUSINESS = "BUSINESS"


class LegalEntityType(StrEnum):
    """The legal type of a recipient account."""

    PERSON = "PERSON"
    BUSINESS = "BUSINESS"


class RecipientAccountResponse(BaseModel):
    """The recipient account as received from the API.

    Attributes:
        id: The ID of the recipient account.
        profileId: ABSENT - replaced by profile
            Personal or business profile ID.
        creatorId: ABSENT - replaced by user.
            Account entity that owns the recipient account
        name: Recipient name details
        currency: 3 character currency code
        type: Recipient type
        legalEntityType: ABSENT - replaced by details.legalType.
            Legal Entity type of recipient
        active: Whether the recipient account is active - Status of the recipient
        details: Recipient account details
        commonFieldMap: Map of key lookup fields on the account
        hash: Account hash for change tracking
        accountSummary: Summary of account details for ease of lookup
        longAccountSummary: Account details summary
        displayFields: Lookup fields
        isInternal: Whether the recipient account is internal
        ownedByCustomer: If recipient account belongs to profile owner

    """

    id: int
    creatorId: DOCUMENTED_BUT_ABSENT[int] = None
    profileId: DOCUMENTED_BUT_ABSENT[int] = None
    name: Optional[RecipientName] = None
    currency: str = CURRENCY
    # country: Optional[str] = COUNTRY_CODE
    type: Annotated[
        AccountRequirementType,
        BeforeValidator(AccountRequirementType.from_camel_case),
    ]
    legalEntityType: DOCUMENTED_BUT_ABSENT[LegalEntityType | LegalType] = None
    active: bool
    commonFieldMap: Optional[CommonFieldMap] = None
    hash: str
    accountSummary: str
    longAccountSummary: str
    displayFields: list[DisplayField]
    isInternal: bool
    ownedByCustomer: bool
    email: Optional[str] = None

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "id": 40000000,
        "creatorId": 41000000,
        "profileId": 30000000,
        "name": {
            "fullName": "John Doe",
            "givenName": null,
            "familyName": null,
            "middleName": null,
            "patronymicName": null,
            "cannotHavePatronymicName": null
        },
        "currency": "GBP",
        "type": "sort_code",
        "legalEntityType": "PERSON",
        "active": true,
        "commonFieldMap": {
            "accountNumberField": "accountNumber",
            "bankCodeField": "sortCode"
        },
        "hash": "666ef880f8aa6113fa112ba6531d3ed2c26dd9fgbd7de5136bfb827a6e800479",
        "accountSummary": "(04-00-75) 37778842",
        "longAccountSummary": "GBP account ending in 8842",
        "displayFields": [
            {
                "key": "details/sortCode",
                "label": "UK sort code",
                "value": "04-00-75"
            },
            {
                "key": "details/accountNumber",
                "label": "Account number",
                "value": "37778842"
            }
        ],
        "isInternal": false,
        "ownedByCustomer": false,
        "email": null
    }
    """


ACCOUNT_HOLDER_NAME_REGEX = r"[0-9A-Za-zÀ-ÖØ-öø-ÿ-_()'*,.\s]+"


class RecipientAccountRequest(BaseModel):
    """Data to create a recipient account.

    Attributes:
        currency: 3 character currency code
        type: Recipient type
        profile: Personal or business profile ID. It is highly advised to pass the
            business profile ID in this field if your business account
            is managed by multiple users, so that the recipient can be
            accessed by all users authorized on the business account.
        ownedByCustomer: Whether this account is owned by the sending user
        accountHolderName: Recipient full name
        details: Currency specific fields
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "currency": "GBP",
        "type": "sort_code",
        "profile": 30000000,
        "ownedByCustomer": true,
        "accountHolderName": "John Doe",
        "details": {
            "dateOfBirth": "1961-01-01",
            "legalType": "PRIVATE",
            "accountNumber": "37778842",
            "sortCode": "040075"
        }
    }
    """

    currency: str = CURRENCY
    type: AccountRequirementType
    profile: int
    ownedByCustomer: bool
    accountHolderName: str = Field(pattern=ACCOUNT_HOLDER_NAME_REGEX)
    details: WithoutNone[RecipientAccountRequestDetails]


class FilledInRecipientAccountRequest(RecipientAccountRequest):
    """The result of creating a recipient.

    Attributes:
        id: Recipient account ID
        business: Business profile ID
        confirmations: unclear
        country: Recipient country code
        user: User ID
        active: Whether the recipient account is active
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "currency": "GBP",
        "type": "sort_code",
        "profile": 30000000,
        "ownedByCustomer": true,
        "accountHolderName": "John Doe",
        "details": {
            "dateOfBirth": "1961-01-01",
            "legalType": "PRIVATE",
            "accountNumber": "37778842",
            "sortCode": "040075"
        },
        "id": 40000000,
        "business": 30000000,
        "confirmations": null,
        "country": "GB",
        "user": 41000000,
        "active": true
    }
    """

    id: int
    business: Optional[int] = None
    confirmations: object # TODO: What is this?
    country: Optional[str] = COUNTRY_CODE
    user: Optional[int] = None
    active: bool


class RecipientAccountsSorting(BaseModel):
    """Sorting configuration."""

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "empty": true,
        "sorted": false,
        "unsorted": true
    }
    """

    empty: bool
    sorted: bool
    unsorted: bool


class RecipientAccountList(BaseModel):
    """A list paginated of recipient accounts."""

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "content": [],
        "sort": {
            "empty": true,
            "sorted": false,
            "unsorted": true
        },
        "size": 0
    }
    """

    content: list[RecipientAccountResponse]
    sort: RecipientAccountsSorting
    size: int


class RecipientAccountRequirements(RequirementsList[AccountRequirement]):
    """An easy access to all the requirements."""


RecipientAccountRequirements._add_getters_from_type(AccountRequirementType, AccountRequirement)

__all__ = [
    "RecipientAccountResponse",
    "RecipientAccountRequest",
    "RecipientAccountRequestDetails",
    "RecipientName",
    "CommonFieldMap",
    "DisplayField",
    "AccountRequirement",
    "RequiredField",
    "LegalType",
    "RecipientAccountList",
    "RecipientAccountsSorting",
    "AccountRequirementType",
    "FilledInRecipientAccountRequest",
    "LegalEntityType",
    "RecipientAccountRequirements",
]
