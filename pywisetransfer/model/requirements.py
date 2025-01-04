"""Requirements for recipients and transfers."""

from typing import ClassVar, Literal, Optional

from pywisetransfer.model.base import BaseModel
from pywisetransfer.model.enum import StrEnum
from pywisetransfer.model.account_requirement_type import AccountRequirementType


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


class RequirementsList(list):
    """A list of requirements."""

    @classmethod
    def _add_getter(cls, requirement_type: str, result_type: type) -> None:
        """Add a getter for a requirement type."""

        def get_requirement(self: cls, requirement_type=requirement_type):
            for requirement in self:
                if requirement.type == requirement_type:
                    return requirement
            return None

        setattr(
            cls,
            str(requirement_type),
            property(get_requirement, doc=f"Get the {requirement_type} requirement if present."),
        )
        cls.__annotations__[str(requirement_type)] = result_type

    @classmethod
    def _add_getters_from_type(cls, type: type[StrEnum], result_type: type) -> None:
        for requirement_type in type:
            cls._add_getter(requirement_type, result_type)


class RequirementBase(BaseModel):
    """A requirement for a recipient account.

    Attributes:
        type: Type of requirement
        title: Display name
        usageInfo: UNKNOWN - Usage information
        fields: List of fields required, grouped together
    """

    type: str
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
        return any(
            group.refreshRequirementsOnChange for field in self.fields for group in field.group
        )


class AccountRequirement(RequirementBase):
    """A requirement for a recipient account.

    Attributes:
        type: Type of requirement
        title: Display name
        usageInfo: UNKNOWN - Usage information
        fields: List of fields required, grouped together
    """

    type: AccountRequirementType
    title: str
    usageInfo: Optional[object]


class TransferRequirement(RequirementBase):
    """A requirement for a transfer.

    Attributes:
        type: Type of requirement
        fields: List of fields required, grouped together

    See https://docs.wise.com/api-docs/api-reference/transfer#transfer-requirements
    """

    type: Literal["transfer"] = "transfer"


class TransferRequirements(RequirementsList[TransferRequirement]):
    """An easy access to all the requirements."""


TransferRequirements._add_getter("transfer", AccountRequirement)


__all__ = [
    "RequiredFieldType",
    "RequiredGroupElement",
    "RequiredField",
    "AllowedValue",
    "RequirementsList",
    "TransferRequirement",
    "TransferRequirements",
    "RequirementBase",
    "AccountRequirement",
]
