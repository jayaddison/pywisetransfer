"""The account models.


See https://docs.wise.com/api-docs/api-reference/recipient

"""

from datetime import date
from typing import ClassVar, Optional

from pydantic import Field
from pywisetransfer.model.base import DOCUMENTED_BUT_ABSENT, BaseModel
from pywisetransfer.model.country import COUNTRY_CODE
from pywisetransfer.model.currency import CURRENCY
from pywisetransfer.model.enum import StrEnum
from pywisetransfer.model.profile import PROFILE_TYPE
from pywisetransfer.model.recipient.details import RecipientDetails
from pywisetransfer.model.requirement_type import RequirementType


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
    type: str
    legalEntityType: DOCUMENTED_BUT_ABSENT[LegalEntityType] = None
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
        "ownedByCustomer": false,
        "email": null
    }
    """


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
    type: RequirementType
    profile: int
    ownedByCustomer: bool
    accountHolderName: str = Field(pattern=ACCOUNT_HOLDER_NAME_REGEX)
    details: RecipientAccountRequestDetails


class FilledInRecipientAccountRequest(RecipientAccountRequest):
    """The result of creating a recipient.

    Attributes:
        id: Recipient account ID
        business: unclear
        confirmations: unclear
        country: Recipient country code
        user: User ID
        active: Whether the recipient account is active
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "currency": "EUR",
        "type": "email",
        "profile": 28577318,
        "ownedByCustomer": false,
        "accountHolderName": "John Doe",
        "details": {
            "legalType": "PRIVATE",
            "sortCode": null,
            "accountNumber": null,
            "dateOfBirth": null
        },
        "id": 700614969,
        "business": null,
        "confirmations": null,
        "country": null,
        "user": 12970746,
        "active": true
    }
    """

    id: int
    business: object  # TODO: What is this?
    confirmations: object  # TODO: What is this?
    country: Optional[str] = COUNTRY_CODE
    user: Optional[int] = None
    active: bool


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


class RequiredGroupElement(BaseModel):
    """An element of a group of requirements to a recipient account.

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
    validationAsync: Optional[str | dict]
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


class RequiredField(BaseModel):
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
                "validationAsync": {
                    "url": "https://api.sandbox.transferwise.tech/v1/validators/bsb-code",
                    "      params": [
                        {
                            "key": "bsbCode",
                            "parameterName": "bsbCode",
                            "required": true
                        }
                    ]
                },
                "valuesAllowed": null
            }
        ]
    }
    """

    name: str
    group: list[RequiredGroupElement]


class RecipientAccountRequirement(BaseModel):
    """A requirement for a recipient account.

    Attributes:
        type: Type of requirement
        title: Display name
        usageInfo: UNKNOWN - Usage information
        fields: List of fields required, grouped together
    """

    type: RequirementType
    title: str
    usageInfo: Optional[object]
    fields: list[RequiredField]
    
    @property
    def required_keys(self) -> list[str]:
        """All keys that are required.
        
        This is a shortcut for the required fields for easier validation.
        """
        return list(sorted({group.key for field in self.required_fields for group in field.group}))

    @property
    def required_fields(self) -> list[RequiredField]:
        """All required fields."""
        return [field for field in self.fields if any(group.required for group in field.group)]

    @property
    def optional_fields(self) -> list[RequiredField]:
        """All fields that are not required."""
        return [field for field in self.fields if not any(group.required for group in field.group)]
        
    @property
    def requires_update(self) -> bool:
        """Whether there is a field which requires one more API interaction to get new requirements.
        
        This refers to refreshRequirementsOnChange:
        Sometimes settings a field creates new requirements.
        """
        return any(group.refreshRequirementsOnChange for field in self.fields for group in field.group)


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


class RecipientAccountRequirements(list[RecipientAccountRequirement]):
    """An easy access to all the requirements."""

for requirement_type in RequirementType:
    def get_requirement(self:RecipientAccountRequirements, requirement_type:RequirementType=requirement_type) -> Optional[RecipientAccountRequirement]:
        for requirement in self:
            if requirement.type == requirement_type:
                return requirement
        return None
    setattr(RecipientAccountRequirements, str(requirement_type), property(get_requirement, doc=f"Get the {requirement_type} requirement if present."))

del requirement_type

__all__ = [
    "RecipientAccountResponse",
    "RecipientAccountRequest",
    "RecipientAccountRequestDetails",
    "RecipientName",
    "CommonFieldMap",
    "DisplayField",
    "RecipientAccountRequirement",
    "RequiredField",
    "RequiredFieldType",
    "AllowedValue",
    "LegalType",
    "RecipientAccountList",
    "RecipientAccountsSorting",
    "RequirementType",
    "RequiredGroupElement",
    "FilledInRecipientAccountRequest",
    "LegalEntityType",
    "RecipientAccountRequirements",
]
