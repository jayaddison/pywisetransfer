"""The Quote resource

See https://docs.wise.com/api-docs/api-reference/quote#object
"""

from __future__ import annotations
from typing import ClassVar, Optional
from pywisetransfer.model.profile import ProfileType
from .enum import StrEnum
from .base import BaseModel
from .uuid import UUID
from .currency import CURRENCY
from .timestamp import Timestamp


class RateType(StrEnum):
    """The rateType of a Quote."""

    FIXED = "FIXED"
    FLOATING = "FLOATING"


class ProvidedAmountType(StrEnum):
    """The providedAmountType of a Quote."""

    SOURCE = "SOURCE"
    TARGET = "TARGET"


class FeeType(StrEnum):
    """The type of a Fee."""

    OVERRIDE = "OVERRIDE"


class Fee(BaseModel):
    """The fee of a PricingConfiguration.

    Attributes:
        type: Identifies the type of fee that will be configured. Options include only OVERRIDE
        variable: The selected variable percentage (in decimal format) that should be used in the pricingConfiguration
        fixed: The selected fixed fee (in source currency) that should be used in the pricingConfiguration
    """

    type: FeeType = FeeType.OVERRIDE
    variable: float
    fixed: float


class PricingConfiguration(BaseModel):
    """The PricingConfiguration oF a Quote.

    Allows for pricing configurations to be overridden by partners on a transfer level.
    Mirrors what was sent in the request.
    """

    fee: Fee

    @classmethod
    def no_fee(cls) -> PricingConfiguration:
        """Return a PricingConfiguration with no fee."""
        return cls(fee=Fee(type=FeeType.OVERRIDE, variable=0.0, fixed=0.0))


class DeliveryDelay(BaseModel):
    """The DeliveryDelay of a PaymentOption."""

    reason: str


class PaymentOptionFee(BaseModel):
    """The fee of a payment option of a quote."""

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "sourceCurrency": "GBP",
        "targetCurrency": "USD",
        "sourceAmount": null,
        "targetAmount": 110,
        "pricingConfiguration": {
            "fee": {
                "type": "OVERRIDE",
                "variable": 0.011,
                "fixed": 15.42
            }
        }
    }
    """
    transferwise: float
    payIn: float
    discount: float
    partner: float
    total: float


class PaymentOptionPrice(BaseModel):
    """The price of a payment option of a quote."""

    EXAMPLE_JSON: ClassVar = """{
        "priceSetId": 238,
        "total": {
          "type": "TOTAL",
          "label": "Total fees",
          "value": {
            "amount": 0.77,
            "currency": "GBP",
            "label:": "0.77 GBP"
          }
        },
        "items": [
          {
            "type": "FEE",
            "label": "fee",
            "value": {
              "amount": 0,
              "currency": "GBP",
              "label": "0 GBP"
            }
          },
          {
            "type": "TRANSFERWISE",
            "label": "Our fee",
            "value": {
              "amount": 3.04,
              "currency": "GBP",
              "label": "3.04 GBP"
            }
          },
          {
            "id": 123,
            "type": "DISCOUNT",
            "value": {
              "amount": -2.27,
              "currency": "GBP",
              "label": "2.27 GBP"
            },
            "label": "Discount applied",
            "explanation": {
              "plainText": "You can have a discount for a number of reasons..."
            }
          }
        ],
        "deferredFee": {
          "amount": 14.79,
          "currency": "BRL"
        },
        "calculatedOn": {
          "unroundedAmountToConvert": {
            "amount": 179.97342,
            "currency": "BRL"
          }
        }
      } 
    """
    priceSetId: int
    total: dict  # TODO: later
    items: list  # TODO: later
    deferredFee: dict
    calculatedOn: dict


class PaymentOption(BaseModel):
    """The PaymentOption of a Quote.

    See https://docs.wise.com/api-docs/api-reference/quote
    """

    EXAMPLE_JSON : ClassVar[str] = """
    {
        "disabled": false,
        "estimatedDelivery": "2019-04-08T10:30:00Z",
        "formattedEstimatedDelivery": "by Apr 8",
        "estimatedDeliveryDelays": [
            {
                "reason": "sample reason"
            }
        ],
        "fee": {
            "transferwise": 3.04,
            "payIn": 0.0,
            "discount": 2.27,
            "partner": 0.0,
            "total": 0.77
        },
        "price": {
            "priceSetId": 238,
            "total": {
                "type": "TOTAL",
                "label": "Total fees",
                "value": {
                    "amount": 0.77,
                    "currency": "GBP",
                    "label:": "0.77 GBP"
                }
            },
            "items": [
                {
                    "type": "FEE",
                    "label": "fee",
                    "value": {
                        "amount": 0,
                        "currency": "GBP",
                        "label": "0 GBP"
                    }
                },
                {
                    "type": "TRANSFERWISE",
                    "label": "Our fee",
                    "value": {
                        "amount": 3.04,
                        "currency": "GBP",
                        "label": "3.04 GBP"
                    }
                },
                {
                    "id": 123,
                    "type": "DISCOUNT",
                    "value": {
                        "amount": -2.27,
                        "currency": "GBP",
                        "label": "2.27 GBP"
                    },
                    "label": "Discount applied",
                    "explanation": {
                        "plainText": "You can have a discount for a number of reasons..."
                    }
                }
            ],
            "deferredFee": {
                "amount": 14.79,
                "currency": "BRL"
            },
            "calculatedOn": {
                "unroundedAmountToConvert": {
                    "amount": 179.97342,
                    "currency": "BRL"
                }
            }
        },
        "sourceAmount": 100,
        "targetAmount": 129.24,
        "sourceCurrency": "GBP",
        "targetCurrency": "USD",
        "payIn": "BANK_TRANSFER",
        "payOut": "BANK_TRANSFER",
        "allowedProfileTypes": [
            "PERSONAL",
            "BUSINESS"
        ],
        "payInProduct": "CHEAP",
        "feePercentage": 0.0092
    }
    """    
    disabled: bool
    estimatedDelivery: Timestamp
    formattedEstimatedDelivery: str
    estimatedDeliveryDelays: list[DeliveryDelay]
    fee: PaymentOptionFee
    price: PaymentOptionPrice
    sourceAmount: int | float
    targetAmount: int | float
    sourceCurrency: str = CURRENCY
    targetCurrency: str = CURRENCY
    payIn: str
    payOut: str
    allowedProfileTypes: list[ProfileType]
    payInProduct: str
    feePercentage: float


class QuoteStatus(StrEnum):
    """The status of a quote."""

    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    FUNDED = "FUNDED"
    EXPIRED = "EXPIRED"


class NoticeType(StrEnum):
    """The type of a notice of a Quote.

    If it is BLOCKED, don't allow the quote to be used to create the transfer.
    """

    WARNING = "WARNING"
    INFO = "INFO"
    BLOCKED = "BLOCKED"


class Notice(BaseModel):

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "text": "You can have a maximum of 3 open transfers with a guaranteed rate. After that, they'll be transferred using the live rate. Complete or cancel your other transfers to regain the use of guaranteed rate.",
        "link": null,
        "type": "WARNING"
    }
    """
    text: str
    link: Optional[str]
    type: NoticeType


class QuoteResponse(BaseModel):
    """The Quote object.

    See https://docs.wise.com/api-docs/api-reference/quote#object
    """

    id: str = UUID
    sourceCurrency: str = CURRENCY
    targetCurrency: str = CURRENCY
    sourceAmount: int | float
    targetAmount: int | float
    payOut: str
    rate: float | int
    createdTime: str
    user: int
    profile: int
    rateType: RateType
    rateExpirationTime: Timestamp
    providedAmountType: ProvidedAmountType
    pricingConfiguration: PricingConfiguration
    paymentOptions: list[PaymentOption]
    status: QuoteStatus
    expirationTime: Timestamp
    notices: list[Notice]


class QuoteRequest(BaseModel):
    """The data that is required to create a quote.

    https://docs.wise.com/api-docs/api-reference/quote#create-not-authenticated

    >>> quote_request = QuoteRequest(sourceCurrency="GBP", targetCurrency="USD", sourceAmount=None, targetAmount=110
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "sourceCurrency": "GBP",
        "targetCurrency": "USD",
        "sourceAmount": null,
        "targetAmount": 110,
        "pricingConfiguration": {
            "fee": {
                "type": "OVERRIDE",
                "variable": 0.011,
                "fixed": 15.42
            }
        }
    }
    """
    sourceCurrency: str = CURRENCY
    targetCurrency: str = CURRENCY
    sourceAmount: Optional[int | float] = None
    targetAmount: Optional[int | float] = None
    pricingConfiguration: PricingConfiguration = PricingConfiguration.no_fee()


__all__ = [
    "QuoteResponse",
    "QuoteStatus",
    "Notice",
    "NoticeType",
    "PaymentOption",
    "PaymentOptionFee",
    "PaymentOptionPrice",
    "PricingConfiguration",
    "ProvidedAmountType",
    "RateType",
    "DeliveryDelay",
    "Fee",
    "FeeType",
    "QuoteRequest",
]
