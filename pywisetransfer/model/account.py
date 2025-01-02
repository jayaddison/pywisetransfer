"""The account models.


See https://docs.wise.com/api-docs/api-reference/recipient

"""

from datetime import date
from typing import ClassVar, Optional

from pydantic import Field
from pywisetransfer.model.base import BaseModel
from pywisetransfer.model.country import COUNTRY_CODE
from pywisetransfer.model.currency import CURRENCY
from pywisetransfer.model.enum import StrEnum
from pywisetransfer.model.profile import PROFILE_TYPE


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
    givenName: Optional[str]
    familyName: Optional[str]
    middleName: Optional[str]
    patronymicName: Optional[str]
    cannotHavePatronymicName: object


class RecipientAccountDetails(BaseModel):
    """The recipient account details.

    Attributes:
        reference: Recipient will see this reference text in their bank statement.
        accountNumber: Recipient account number
        sortCode: Recipient sort code
        hashedByLooseHashAlgorithm: Recipient account hash
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "reference": null,
        "accountNumber": "37778842",
        "sortCode": "040075",
        "hashedByLooseHashAlgorithm": "ad245621b974efa3ef870895c3wer419a3f01af18a8a5790b47645dba6304194"
    }
    """

    reference: Optional[str] = None
    accountNumber: Optional[str] = None
    sortCode: Optional[str] = None
    hashedByLooseHashAlgorithm: str


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


class RecipientAccountResponse(BaseModel):
    """The recipient account.

    Attributes:
        id: The ID of the recipient account.
        creatorId: Account entity that owns the recipient account
        name: Recipient name details
        currency: 3 character currency code
        country: 2 character country code
        type: Recipient type
        legalEntityType: Entity type of recipient
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
    creatorId: int
    profileId: int
    name: RecipientName
    currency: str = CURRENCY
    country: str = COUNTRY_CODE
    type: str
    legalEntityType: str
    active: bool
    commonFieldMap: CommonFieldMap
    hash: str
    accountSummary: str
    longAccountSummary: str
    displayFields: list[DisplayField]
    isInternal: bool
    ownedByCustomer: bool

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
        "country": "GB",
        "type": "SortCode",
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
        "ownedByCustomer": false
    }
    """
    id: int


class LegalType(StrEnum):
    """The legal type of a recipient account."""
    PRIVATE = "PRIVATE"
    BUSINESS = "BUSINESS"


class RecipientAccountRequestDetails(BaseModel):
    """Details to create a recipient account.

    Attributes:
        legalType: Recipient legal type: PRIVATE or BUSINESS
        sortCode: Recipient bank sort code (GBP)
        accountNumber: Recipient bank account no (GBP)
        dateOfBirth: Recipient Date of Birth in ISO 8601 date format.
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "legalType": "PRIVATE",
        "sortCode": "040075",
        "accountNumber": "37778842",
        "dateOfBirth": "1961-01-01"
    }
    """
    legalType: LegalType
    sortCode: Optional[str] = None
    accountNumber: Optional[str] = None
    dateOfBirth: Optional[date] = None


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
            "legalType": "PRIVATE",
            "sortCode": "040075",
            "accountNumber": "37778842",
            "dateOfBirth": "1961-01-01"
        }
    }
    """

    currency: str = CURRENCY
    type: str
    profile: int
    ownedByCustomer: bool
    accountHolderName: str = Field(pattern=ACCOUNT_HOLDER_NAME_REGEX)
    details: RecipientAccountRequestDetails


class RequiredFieldType(StrEnum):
    """Type of a recipient account requirement."""

    text = "text"
    select = "select"
    date = "date"
    radio = "radio"


class AllowedValue(BaseModel):
    """Allowed value for a recipient account requirement.

    Attributes:
        key: JSON key
        name: Display name
    """

    key: str
    name: str

    def is_valid(self):
        """Whether you can use this key."""
        return self.key != ""


class RequiredField(BaseModel):
    """A single requirement to a recipient account.

    Attributes:
        name: Field description
        key: Key is name of the field you should include in the JSON
        type: Display type of field. Can be text, select, radio or date
        refreshRequirementsOnChange: Tells you whether you should call POST account-requirements once the field value is set to discover required lower level fields.
        required: Whether the field is required or not
        displayFormat: Display format pattern.
        example: Example value
        minLength: Minimum length
        maxLength: Maximum length
        validationRegexp: Regexp validation pattern.
        validationAsync: Validator URL and parameter name you should use when submitting the value for validation
        valuesAllowed: List of allowed values.
    """

    key: str
    name: str
    type: RequiredFieldType
    refreshRequirementsOnChange: bool
    required: bool
    displayFormat: Optional[str]
    example: str
    minLength: Optional[int]
    maxLength: Optional[int]
    validationRegexp: Optional[str]
    validationAsync: Optional[str]
    valuesAllowed: Optional[list[AllowedValue]]

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "key": "address.country",
        "name": "Country",
        "type": "select",
        "refreshRequirementsOnChange": true,
        "required": true,
        "displayFormat": null,
        "example": "Choose a country",
        "minLength": null,
        "maxLength": null,
        "validationRegexp": null,
        "validationAsync": null,
        "valuesAllowed": [
            {
                "key": "GB",
                "name": "United Kingdom"
            }
        ]
    }
    """


class RecipientAccountRequirement(BaseModel):
    """Requirements for a recipient account."""

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "name": "City",
        "group": [
            {
                "key": "address.city",
                "name": "City",
                "type": "text",
                "refreshRequirementsOnChange": false,
                "required": true,
                "displayFormat": null,
                "example": "",
                "minLength": 1,
                "maxLength": 255,
                "validationRegexp": "^.{1,255}$",
                "validationAsync": null,
                "valuesAllowed": null
            }
        ]
    }
    """

    name: str
    group: list[RequiredField]


__all__ = [
    "RecipientAccountResponse",
    "RecipientAccountRequest",
    "RecipientAccountRequestDetails",
    "RecipientAccountDetails",
    "RecipientName",
    "CommonFieldMap",
    "DisplayField",
    "RecipientAccountRequirement",
    "RequiredField",
    "RequiredFieldType",
    "AllowedValue",
    "LegalType",
]
