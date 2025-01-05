"""The Quote resource

See https://docs.wise.com/api-docs/api-reference/quote#object
"""

from __future__ import annotations
from typing import ClassVar, Optional
from pywisetransfer.model.profile import PROFILE_TYPE
from .enum import StrEnum
from .base import DOCUMENTED_BUT_ABSENT, BaseModel
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


class PriceType(StrEnum):
    """The type of a Fee.

    Attributes:
        OVERRIDE: The type of fee you can set yourself in the pricing configuration.
    """

    OVERRIDE = "OVERRIDE"
    PAYIN = "PAYIN"
    TOTAL = "TOTAL"
    TRANSFERWISE = "TRANSFERWISE"
    VAT = "VAT"
    DISCOUNT = "DISCOUNT"
    FEE = "FEE"


class PricingConfigurationFee(BaseModel):
    """The fee of a PricingConfiguration.

    Attributes:
        type: Identifies the type of fee that will be configured. Options include only OVERRIDE
        variable: The selected variable percentage (in decimal format) that should be used in the pricingConfiguration
        fixed: The selected fixed fee (in source currency) that should be used in the pricingConfiguration
    """

    EXAMPLE_JSON = """
    {
        "type": "OVERRIDE",
        "variable": 0.011,
        "fixed": 15.42
    }
    """

    type: PriceType = PriceType.OVERRIDE
    variable: float = 0
    fixed: float = 0


class PricingConfiguration(BaseModel):
    """The PricingConfiguration oF a Quote.

    Allows for pricing configurations to be overridden by partners on a transfer level.
    Mirrors what was sent in the request.
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "fee": {
            "type": "OVERRIDE",
            "variable": 0.011,
            "fixed": 15.42
        }
    }
    """

    fee: PricingConfigurationFee

    @classmethod
    def no_fee(cls) -> PricingConfiguration:
        """Return a PricingConfiguration with no fee."""
        return cls(fee=PricingConfigurationFee(type=PriceType.OVERRIDE, variable=0.0, fixed=0.0))


class DeliveryDelay(BaseModel):
    """The DeliveryDelay of a PaymentOption."""

    reason: str


class PaymentOptionFee(BaseModel):
    """The fee of a payment option of a quote."""

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "transferwise": 3.04,
        "payIn": 0.0,
        "discount": 2.27,
        "partner": 0.0,
        "total": 0.77
    }
    """
    transferwise: float
    payIn: float
    discount: float
    partner: float
    total: float


class PriceValue(BaseModel):
    """The value of a price.

    Attributes:
        amount: The amount of the value.
        currency: The currency of the value.
        label: The label of the value
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "amount": 0.77,
        "currency": "GBP",
        "label": "0.77 GBP"
    }
    """
    amount: float
    currency: str = CURRENCY
    label: str


class Price(BaseModel):
    """The total fees of a payment option of a quote.

    Attributes:
        type: Type of the fee.
        label: Label of the fee.
        value: Value of the fee.
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "type": "TOTAL",
        "label": "Total fees",
        "value": {
            "amount": 0.77,
            "currency": "GBP",
            "label": "0.77 GBP"
        }
    }
    """

    type: PriceType
    label: str
    value: PriceValue


class PaymentOptionPrice(BaseModel):
    """The price of a payment option of a quote."""

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "priceSetId": 238,
        "total": {
            "type": "TOTAL",
            "label": "Total fees",
            "value": {
                "amount": 0.77,
                "currency": "GBP",
                "label": "0.77 GBP"
            }
        },
        "items": [
            {
                "type": "FEE",
                "label": "fee",
                "value": {
                    "amount": 0.0,
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
                "type": "DISCOUNT",
                "label": "Discount applied",
                "value": {
                    "amount": -2.27,
                    "currency": "GBP",
                    "label": "2.27 GBP"
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
    total: Price
    items: list[Price]
    deferredFee: Optional[dict] = None
    calculatedOn: Optional[dict] = None


class PaymentOption(BaseModel):
    """The PaymentOption of a Quote.

    See https://docs.wise.com/api-docs/api-reference/quote
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
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
                    "label": "0.77 GBP"
                }
            },
            "items": [
                {
                    "type": "FEE",
                    "label": "fee",
                    "value": {
                        "amount": 0.0,
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
                    "type": "DISCOUNT",
                    "label": "Discount applied",
                    "value": {
                        "amount": -2.27,
                        "currency": "GBP",
                        "label": "2.27 GBP"
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
    estimatedDelivery: Optional[Timestamp] = None
    formattedEstimatedDelivery: Optional[str] = None
    estimatedDeliveryDelays: list[DeliveryDelay]
    fee: PaymentOptionFee
    price: PaymentOptionPrice
    sourceAmount: int | float
    targetAmount: int | float
    sourceCurrency: str = CURRENCY
    targetCurrency: str = CURRENCY
    payIn: PaymentMethod
    payOut: PaymentMethod
    allowedProfileTypes: list[PROFILE_TYPE]
    payInProduct: Optional[PayInProduct] = None
    feePercentage: float


class PayInProduct(StrEnum):
    """The product to use to pay in for a quote."""

    # generated from
    # grep -roE 'payInProduct":[^,]+' pywisetransfer/ | grep -oE '"[^"]+"$' | sort | uniq
    ADVANCED = "ADVANCED"
    BALANCE = "BALANCE"
    CHEAP = "CHEAP"
    EASY = "EASY"
    FAST = "FAST"
    JUST_FAST = "JUST_FAST"


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

    Quote Response
    --------------

    The following describes the fields of the quote response that may be useful
    when building your integration.

    The payOut field is used to select the correct entry in the paymentOptions array
    in order to know which fees to display to your customer. Find the paymentOption
    that matches the payOut field shown at the top level of the quote resource and payIn
    based on the settlement model the bank is using. By default, this is BANK_TRANSFER,
    unless you are using a prefunded or bulk settlement model. The payOut field will change
    based on the type of recipient you add to the quote in the PATCH /quote call,
    for example to-USD swift_code or to-CAD interac have different fees.

    For example sending USD to a country other than the United States is supported but
    with different fees to domestic USD transfers. Please see the later section on
    Global Currencies to learn more about how to offer this useful feature.

    For each paymentOption there is a price field. It gives a full breakdown of all the taxes,
    fees and discounts. It is preferable to refer to this structure to show breakdowns and
    totals, rather than the fee structure, found as well in each paymentOption element,
    that only gives a summary and is not able to surface important specifics such as taxes.

    When showing the price of a transfer always show the 'price.total.value.amount' of a payment option.

    Disabled Payment Options
    ------------------------

    Each payment option is either enabled or disabled based on the disabled value.
    Disabled payment options should be shown to the user in a disabled state in most cases.
    This ensures users are given the options that they are familiar with regardless of their
    availability, as well as with options that can be beneficial to their accounts.

    The option.disabledReason contains both the code and message, with the message
    being the user-friendly text to surface to the user if necessary.

    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "id": "476e55ac-de76-4712-909b-5e6f44beb5ad",
        "sourceCurrency": "GBP",
        "targetCurrency": "USD",
        "sourceAmount": null,
        "targetAmount": 110.0,
        "payOut": "BANK_TRANSFER",
        "rate": 1.24256,
        "createdTime": "2025-01-03T21:29:16Z",
        "user": 12970746,
        "profile": null,
        "rateType": "FIXED",
        "rateExpirationTime": "2025-01-06T08:59:59Z",
        "providedAmountType": "TARGET",
        "pricingConfiguration": null,
        "paymentOptions": [
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 0.59,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 1.99
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 1.99,
                            "currency": "GBP",
                            "label": "1.99 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 1.99,
                                "currency": "GBP",
                                "label": "1.99 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 90.52,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "DEBIT",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "FAST",
                "feePercentage": 0.022
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 2.05,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 3.45
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 3.45,
                            "currency": "GBP",
                            "label": "3.45 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 3.45,
                                "currency": "GBP",
                                "label": "3.45 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 91.98,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "CREDIT",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "FAST",
                "feePercentage": 0.0375
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 0.0,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 1.4
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 1.4,
                            "currency": "GBP",
                            "label": "1.40 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 1.4,
                                "currency": "GBP",
                                "label": "1.40 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 89.93,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "BANK_TRANSFER",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "CHEAP",
                "feePercentage": 0.0156
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 0.0,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 1.4
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 1.4,
                            "currency": "GBP",
                            "label": "1.40 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 1.4,
                                "currency": "GBP",
                                "label": "1.40 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 89.93,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "PISP",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "CHEAP",
                "feePercentage": 0.0156
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-07T17:30:00Z",
                "formattedEstimatedDelivery": "by Tuesday, January 7",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 0.0,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 1.4
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 1.4,
                            "currency": "GBP",
                            "label": "1.40 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 1.4,
                                "currency": "GBP",
                                "label": "1.40 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 89.93,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "SWIFT",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "ADVANCED",
                "feePercentage": 0.0156
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 0.33,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 1.73
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 1.73,
                            "currency": "GBP",
                            "label": "1.73 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 1.73,
                                "currency": "GBP",
                                "label": "1.73 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 90.26,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "VISA_DEBIT_OR_PREPAID",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "FAST",
                "feePercentage": 0.0192
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 4.93,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 6.33
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 6.33,
                            "currency": "GBP",
                            "label": "6.33 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 6.33,
                                "currency": "GBP",
                                "label": "6.33 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 94.86,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "INTERNATIONAL_DEBIT",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "FAST",
                "feePercentage": 0.0667
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 3.69,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 5.09
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 5.09,
                            "currency": "GBP",
                            "label": "5.09 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 5.09,
                                "currency": "GBP",
                                "label": "5.09 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 93.62,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "MC_BUSINESS_CREDIT",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "FAST",
                "feePercentage": 0.0544
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 0.59,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 1.99
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 1.99,
                            "currency": "GBP",
                            "label": "1.99 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 1.99,
                                "currency": "GBP",
                                "label": "1.99 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 90.52,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "MC_DEBIT_OR_PREPAID",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "FAST",
                "feePercentage": 0.022
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 1.13,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 2.53
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 2.53,
                            "currency": "GBP",
                            "label": "2.53 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 2.53,
                                "currency": "GBP",
                                "label": "2.53 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 91.06,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "MC_CREDIT",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "FAST",
                "feePercentage": 0.0278
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 0.59,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 1.99
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 1.99,
                            "currency": "GBP",
                            "label": "1.99 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 1.99,
                                "currency": "GBP",
                                "label": "1.99 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 90.52,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "CARD",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "FAST",
                "feePercentage": 0.022
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 0.59,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 1.99
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 1.99,
                            "currency": "GBP",
                            "label": "1.99 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 1.99,
                                "currency": "GBP",
                                "label": "1.99 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 90.52,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "MAESTRO",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "FAST",
                "feePercentage": 0.022
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 2.94,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 4.34
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 4.34,
                            "currency": "GBP",
                            "label": "4.34 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 4.34,
                                "currency": "GBP",
                                "label": "4.34 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 92.87,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "MC_BUSINESS_DEBIT",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "FAST",
                "feePercentage": 0.0467
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 3.69,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 5.09
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 5.09,
                            "currency": "GBP",
                            "label": "5.09 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 5.09,
                                "currency": "GBP",
                                "label": "5.09 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 93.62,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "VISA_BUSINESS_CREDIT",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "FAST",
                "feePercentage": 0.0544
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 1.39,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 2.79
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 2.79,
                            "currency": "GBP",
                            "label": "2.79 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 2.79,
                                "currency": "GBP",
                                "label": "2.79 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 91.32,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "VISA_BUSINESS_DEBIT",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "FAST",
                "feePercentage": 0.0306
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 4.93,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 6.33
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 6.33,
                            "currency": "GBP",
                            "label": "6.33 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 6.33,
                                "currency": "GBP",
                                "label": "6.33 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 94.86,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "INTERNATIONAL_CREDIT",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "FAST",
                "feePercentage": 0.0667
            },
            {
                "disabled": false,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.4,
                    "payIn": 2.05,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 3.45
                },
                "price": {
                    "priceSetId": 384,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 3.45,
                            "currency": "GBP",
                            "label": "3.45 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 3.45,
                                "currency": "GBP",
                                "label": "3.45 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 91.98,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "VISA_CREDIT",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "FAST",
                "feePercentage": 0.0375
            },
            {
                "disabled": true,
                "estimatedDelivery": "2025-01-06T17:30:00Z",
                "formattedEstimatedDelivery": "by Monday, January 6",
                "estimatedDeliveryDelays": [],
                "fee": {
                    "transferwise": 1.23,
                    "payIn": 0.0,
                    "discount": 0.0,
                    "partner": 0.0,
                    "total": 1.23
                },
                "price": {
                    "priceSetId": 381,
                    "total": {
                        "type": "TOTAL",
                        "label": "Total fees",
                        "value": {
                            "amount": 1.23,
                            "currency": "GBP",
                            "label": "1.23 GBP"
                        }
                    },
                    "items": [
                        {
                            "type": "TRANSFERWISE",
                            "label": "Our fee",
                            "value": {
                                "amount": 1.23,
                                "currency": "GBP",
                                "label": "1.23 GBP"
                            }
                        }
                    ],
                    "deferredFee": null,
                    "calculatedOn": null
                },
                "sourceAmount": 89.76,
                "targetAmount": 110.0,
                "sourceCurrency": "GBP",
                "targetCurrency": "USD",
                "payIn": "BALANCE",
                "payOut": "BANK_TRANSFER",
                "allowedProfileTypes": [
                    "PERSONAL",
                    "BUSINESS"
                ],
                "payInProduct": "BALANCE",
                "feePercentage": 0.0137
            }
        ],
        "status": "PENDING",
        "expirationTime": "2025-01-03T21:59:16Z",
        "notices": []
    }
    """

    id: str = UUID
    sourceCurrency: str = CURRENCY
    targetCurrency: str = CURRENCY
    sourceAmount: DOCUMENTED_BUT_ABSENT[int | float] = None
    targetAmount: DOCUMENTED_BUT_ABSENT[int | float] = None
    payOut: PaymentMethod
    rate: float | int
    createdTime: Timestamp | None
    user: int
    profile: DOCUMENTED_BUT_ABSENT[int] = None
    rateType: RateType
    rateExpirationTime: Timestamp | None
    providedAmountType: ProvidedAmountType
    pricingConfiguration: DOCUMENTED_BUT_ABSENT[PricingConfiguration] = None
    paymentOptions: list[PaymentOption]
    status: QuoteStatus
    expirationTime: Timestamp | None
    notices: list[Notice]
    
    @property
    def enabled_payments(self) -> list[PaymentOption]:
        """A list of payment options that can be used."""
        return [payment_option for payment_option in self.paymentOptions if not payment_option.disabled]


class ExampleQuoteRequest(BaseModel):
    """The data that is required to create an example quote.

    https://docs.wise.com/api-docs/api-reference/quote#create-not-authenticated

    >>> from pywisetransfer import ExampleQuoteRequest
    >>> quote_request = ExampleQuoteRequest(
    ...     sourceCurrency="GBP",
    ...     targetCurrency="USD",
    ...     sourceAmount=None,
    ...     targetAmount=110
    ... )

    Attributes:
        sourceCurrency: Source (sending) currency code.
        targetCurrency: Target (receiving) currency code.
        targetAmount: Amount in target currency.
        sourceAmount: Amount in source currency.
            Either sourceAmount or targetAmount is required, never both.
        pricingConfiguration: Identifies the type of fee that will be configured. Options include only OVERRIDE

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


class PaymentMethod(StrEnum):
    """The preferred payout/payin method."""

    SWIFT_OUR = "SWIFT_OUR"

    # These are generated by this script:
    # grep -roE '"payIn":"[^"]+' pywisetransfer/ | grep -oE '[^"]+$' |sort | uniq

    ALIPAY = "ALIPAY"
    APPLE_PAY = "APPLE_PAY"
    BALANCE = "BALANCE"
    BANK_TRANSFER = "BANK_TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CARD = "CARD"
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"
    DIRECT_DEBIT = "DIRECT_DEBIT"
    FAST_DIRECT_DEBIT = "FAST_DIRECT_DEBIT"
    FPX = "FPX"
    GOOGLE_PAY = "GOOGLE_PAY"
    IDEAL = "IDEAL"
    INT_CREDIT_WITH_EUROPEAN_CARD = "INT_CREDIT_WITH_EUROPEAN_CARD"
    INT_DEBIT_WITH_EUROPEAN_CARD = "INT_DEBIT_WITH_EUROPEAN_CARD"
    INTERAC = "INTERAC"
    INTERNATIONAL_CREDIT = "INTERNATIONAL_CREDIT"
    INTERNATIONAL_DEBIT = "INTERNATIONAL_DEBIT"
    MAESTRO = "MAESTRO"
    MC_BUSINESS_CREDIT = "MC_BUSINESS_CREDIT"
    MC_BUSINESS_DEBIT = "MC_BUSINESS_DEBIT"
    MC_CREDIT = "MC_CREDIT"
    MC_DEBIT_OR_PREPAID = "MC_DEBIT_OR_PREPAID"
    OSKO = "OSKO"
    PAYNOW = "PAYNOW"
    PISP = "PISP"
    POLI = "POLI"
    SWIFT = "SWIFT"
    TRUSTLY = "TRUSTLY"
    VISA_BUSINESS_CREDIT = "VISA_BUSINESS_CREDIT"
    VISA_BUSINESS_DEBIT = "VISA_BUSINESS_DEBIT"
    VISA_CREDIT = "VISA_CREDIT"
    VISA_DEBIT_OR_PREPAID = "VISA_DEBIT_OR_PREPAID"


class PaymentMetadata(BaseModel):
    """Payment metadata in a quote.

    Attributes:
        transferNature: Used to pass transfer nature for calculating proper tax amounts (IOF) for transfers to and from BRL.
            Accepted values are shown dynamically in transfer requirements.
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "transferNature": "MOVING_MONEY_BETWEEN_OWN_ACCOUNTS"
    }
    """
    transferNature: str = "MOVING_MONEY_BETWEEN_OWN_ACCOUNTS"


class QuoteRequest(ExampleQuoteRequest):
    """The data that is required to create a quote.

    This quote is authenticated and can be used to create a transfer.

    >>> from pywisetransfer import QuoteRequest
    >>> quote_request = QuoteRequest(
    ...     sourceCurrency="GBP",
    ...     targetCurrency="USD",
    ...     sourceAmount=None,
    ...     targetAmount=110
    ... )

    Attributes:
        sourceCurrency: Source (sending) currency code.
        targetCurrency: Target (receiving) currency code.
        targetAmount: Amount in target currency.
        sourceAmount: Amount in source currency.
            Either sourceAmount or targetAmount is required, never both.
        pricingConfiguration: Identifies the type of fee that will be configured. Options include only OVERRIDE
        targetAccount: This is the ID of transfer recipient,
            found in response from POST v1/accounts (recipient creation).
            If provided can be used as an alternative to updating the quote.
            https://docs.wise.com/api-docs/api-reference/quote#update
        payOut: Preferred payout method. Default value is PaymentMethod.BANK_TRANSFER.
        preferredPayIn: Preferred payin method.
            Use PaymentMethod.BANK_TRANSFER to return this method at the top of the response's results.
        paymentMetadata: Used to pass additional metadata about the intended transfer.

    If you are funding the transfer from a Multi Currency Balance, you must set the payIn as
    PaymentMethod.BALANCE to get the correct pricing in the quote.
    Not doing so will default to PaymentMethod.BANK_TRANSFER and the fees will be
    inconsistent between quote and transfer.

    When SWIFT_OUR is set as payOut value, it enables payment protection for swift recipients
    for global currency transfers. By using this payOut method, you can guarantee your
    customers that the fee will be charged to the sender and can ensure that the recipient
    gets the complete target amount.
    """

    targetAccount: Optional[int] = None
    payOut: Optional[PaymentMethod] = None
    preferredPayIn: Optional[PaymentMethod] = None
    paymentMetadata: Optional[PaymentMetadata] = None

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "sourceCurrency": "GBP",
        "targetCurrency": "USD",
        "sourceAmount": 100,
        "targetAmount": null,
        "pricingConfiguration": {
            "fee": {
                "type": "OVERRIDE",
                "variable": 0.011,
                "fixed": 15.42
            }
        },
        "targetAccount": 12345,
        "payOut": null,
        "preferredPayIn": null,
        "paymentMetadata": {
            "transferNature": "MOVING_MONEY_BETWEEN_OWN_ACCOUNTS"
        }
    }
    """


class QuoteUpdate(BaseModel):
    """Data required to update a quote.

    See https://docs.wise.com/api-docs/api-reference/quote#update

    Attributes:
        targetAccount: ID of transfer recipient, found in response from POST v1/accounts (recipient creation)
        payOut: Preferred payout method. Default value is PaymentMethod.BANK_TRANSFER.
        paymentMetadata: Used to pass additional metadata about the intended transfer.
        pricingConfiguration: Required when configured for your client ID.
            Includes a pricingConfiguration to be used for pricing calculations with the quote.
            If previously passed, the existing pricingConfiguration will remain and not be updated.
    """

    EXAMPLE_JSON: ClassVar[
        str
    ] = """
    {
        "targetAccount": 12345,
        "payOut": "SWIFT_OUR",
        "paymentMetadata": {
            "transferNature": "MOVING_MONEY_BETWEEN_OWN_ACCOUNTS"
        },
        "pricingConfiguration": {
            "fee": {
                "type": "OVERRIDE",
                "variable": 0.011,
                "fixed": 15.42
            }
        }
    }
    """

    targetAccount: int
    payOut: Optional[PaymentMethod] = None
    paymentMetadata: Optional[PaymentMetadata] = None
    pricingConfiguration: Optional[PricingConfiguration] = None


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
    "PricingConfigurationFee",
    "PriceType",
    "ExampleQuoteRequest",
    "QuoteRequest",
    "PaymentMethod",
    "PaymentMetadata",
    "QuoteUpdate",
    "Price",
    "PriceValue",
    "PayInProduct",
]
