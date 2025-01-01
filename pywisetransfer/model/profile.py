from datetime import date
from typing import ClassVar, Optional, Union
from typing_extensions import Annotated

from pydantic import BeforeValidator, Field
from pywisetransfer.model.base import BaseModel, DEPRECATED
from .enum import StrEnum


class PROFILE_TYPE(StrEnum):
    """The type of profile."""

    PERSONAL = "PERSONAL"
    BUSINESS = "BUSINESS"

class profile_type(StrEnum):
    """The type of profile."""

    personal = "personal"
    business = "business"


class OccupationFormat(StrEnum):
    """The format of an occupation."""
    
    FREE_FORM = "FREE_FORM"

class Occupation(BaseModel):
    """The occupation of a person.
    
    Attributes:
        code: User occupation, any value permitted.
        format: Occupation format
    """
    
    code: str
    format: OccupationFormat = OccupationFormat.FREE_FORM
    

class PersonalProfileDetails(BaseModel):
    """The details of a personal profile.
    
    Attributes:
        firstName: First name
        lastName: Last name
        dateOfBirth: Date of birth
        phoneNumber: Phone number
        avatar: Link to person avatar image
        occupation: DEPRECATED
        occupations: List of occupations, currently one FREE_FORM occupation is supported.
        primaryAddress: Address object ID
        firstNameInKana: First name in Katakana (required for from JPY personal transfers)
        lastNameInKana: Last name in Katakana (required for from JPY personal transfers)
        
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "firstName": "Oliver",
        "lastName": "Wilson",
        "dateOfBirth": "1977-07-01",
        "phoneNumber": "+3725064992",
        "avatar": "",
        "occupation": "",
        "occupations": null,
        "primaryAddress": null,
        "firstNameInKana": null,
        "lastNameInKana": null
    }
    """

    firstName: str
    lastName: str
    dateOfBirth: date
    phoneNumber: str
    avatar: Optional[str]
    occupation: DEPRECATED[str]
    occupations: Optional[list[Occupation]]
    primaryAddress: Optional[int]
    firstNameInKana: Optional[str]
    lastNameInKana: Optional[str]
    
class CompanyType(StrEnum):
    """The type of a company."""
    
    LIMITED = "LIMITED"
    PARTNERSHIP = "PARTNERSHIP"
    SOLE_TRADER = "SOLE_TRADER"
    LIMITED_BY_GUARANTEE = "LIMITED_BY_GUARANTEE"
    LIMITED_LIABILITY_COMPANY = "LIMITED_LIABILITY_COMPANY"
    FOR_PROFIT_CORPORATION = "FOR_PROFIT_CORPORATION"
    NON_PROFIT_CORPORATION = "NON_PROFIT_CORPORATION"
    LIMITED_PARTNERSHIP = "LIMITED_PARTNERSHIP"
    LIMITED_LIABILITY_PARTNERSHIP = "LIMITED_LIABILITY_PARTNERSHIP"
    GENERAL_PARTNERSHIP = "GENERAL_PARTNERSHIP"
    SOLE_PROPRIETORSHIP = "SOLE_PROPRIETORSHIP"
    PRIVATE_LIMITED_COMPANY = "PRIVATE_LIMITED_COMPANY"
    PUBLIC_LIMITED_COMPANY = "PUBLIC_LIMITED_COMPANY"
    TRUST = "TRUST"
    OTHER = "OTHER"


class CompanyRole(StrEnum):
    """Role of person in a company."""
    
    OWNER = "OWNER"
    DIRECTOR = "DIRECTOR"
    OTHER = "OTHER"


class BusinessCategory(StrEnum):
    """The category of a business."""
    
    CHARITY_NON_PROFIT = "CHARITY_NON_PROFIT"
    CONSULTING_IT_BUSINESS_SERVICES = "CONSULTING_IT_BUSINESS_SERVICES"
    DESIGN_MARKETING_COMMUNICATIONS = "DESIGN_MARKETING_COMMUNICATIONS"
    MEDIA_COMMUNICATION_ENTERTAINMENT = "MEDIA_COMMUNICATION_ENTERTAINMENT"
    EDUCATION_LEARNING = "EDUCATION_LEARNING"
    FINANCIAL_SERVICES_PRODUCTS_HOLDING_COMPANIES = "FINANCIAL_SERVICES_PRODUCTS_HOLDING_COMPANIES"
    FOOD_BEVERAGES_TOBACCO = "FOOD_BEVERAGES_TOBACCO"
    HEALTH_PHARMACEUTICALS_PERSONAL_CARE = "HEALTH_PHARMACEUTICALS_PERSONAL_CARE"
    PUBLIC_GOVERNMENT_SERVICES = "PUBLIC_GOVERNMENT_SERVICES"
    REAL_ESTATE_CONSTRUCTION = "REAL_ESTATE_CONSTRUCTION"
    RETAIL_WHOLESALE_MANUFACTURING = "RETAIL_WHOLESALE_MANUFACTURING"
    TRAVEL_TRANSPORT_TOUR_AGENCIES = "TRAVEL_TRANSPORT_TOUR_AGENCIES"
    OTHER = "OTHER"

class BusinessProfileDetails(BaseModel):
    """The details of a business profile.
    
    Attributes:
        name: Business name
        registrationNumber: Business registration number
        acn: Australian Company Number (only for Australian businesses)
        abn: Australian Business Number (only for Australian businesses)
        arbn: Australian Registered Business Number (only for Australian businesses)
        companyType: Company type
        companyRole: Business role  
        descriptionOfBusiness: Business free form description. *Required if companyType is OTHER. If this is not provided for an OTHER companyType, the profile should not be allowed to create a transfer. For the rest of the companyType(s), it is highly recommended to always provide the business' description, to avoid payment issues such as suspensions.
        webpage: Business webpage. *Required if companyType is OTHER. If this is not provided for an OTHER companyType, the profile should not be allowed to create a transfer. For the rest of the companyTypes, it is highly recommended to always provide the business' website,to avoid payment issues such as suspensions.
        primaryAddress: Id of the primary address
        businessCategory: Ensure when submitting a business profile that you submit a category.
        businessSubCategory: Ensure when submitting a business profile that you submit a subcategory.
            See https://docs.wise.com/api-docs/api-reference/profile
    """
    
    name: str
    registrationNumber: str
    acn: Optional[str]
    abn: Optional[str]
    arbn: Optional[str]
    companyType: CompanyType
    companyRole: CompanyRole
    descriptionOfBusiness: Optional[str]
    webpage: Optional[str]
    primaryAddress: Optional[int]
    businessCategory: BusinessCategory
    businessSubCategory: str

   
    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "name": "ABC Logistics Ltd",
        "registrationNumber": "12144939",
        "acn": null,
        "abn": null,
        "arbn": null,
        "companyType": "LIMITED",
        "companyRole": "OWNER",
        "descriptionOfBusiness": "Information and communication",
        "webpage": "https://abc-logistics.com",
        "primaryAddress": 4000001,
        "businessCategory": "CONSULTING_IT_BUSINESS_SERVICES",
        "businessSubCategory": "DESIGN"
    }
    """

class Profile(BaseModel):
    """A profile."""
    
    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "id": 30000001,
        "type": "personal",
        "details": {
            "firstName": "Oliver",
            "lastName": "Wilson",
            "dateOfBirth": "1977-07-01",
            "phoneNumber": "+3725064992",
            "avatar": "",
            "occupation": "",
            "occupations": null,
            "primaryAddress": null,
            "firstNameInKana": null,
            "lastNameInKana": null
        }
    }
    """
    id: int
    type: profile_type
    details: Annotated[
    Union[PersonalProfileDetails, BusinessProfileDetails],
    BeforeValidator(lambda d: PersonalProfileDetails(**d) if "firstName" in d else BusinessProfileDetails(**d))
    ]
    
    def is_personal(self) -> bool:
        """Whether the profile is personal."""
        return self.type == profile_type.personal
    
    def is_business(self) -> bool:
        """Whether the profile is personal."""
        return self.type == profile_type.business

    
class Profiles(list[Profile]):
    """A list of profiles.
    
    Attributes:
        personal: Personal profiles.
        business: Business profiles.
    """
    
    @property
    def personal(self) -> list[Profile]:
        """Personal profiles."""
        return [p for p in self if p.type == profile_type.personal]

    @property
    def business(self) -> list[Profile]:
        """Business profiles."""
        return [p for p in self if p.type == profile_type.business]

__all__ = ["PROFILE_TYPE", "Profile", "PersonalProfileDetails", "profile_type", "BusinessProfileDetails", "BusinessCategory", "CompanyType", "CompanyRole", "Profiles", "Occupation", "OccupationFormat"]
