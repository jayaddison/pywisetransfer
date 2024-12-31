"""Tests for the quotes."""

from pywisetransfer.model.quote import QuoteRequest, QuoteResponse


EXAMPLE_RESPONSE = {
    "clientId": "transferwise-personal-tokens",
    "createdTime": "2024-12-31T17:21:44Z",
    "expirationTime": "2024-12-31T17:51:44Z",
    "funding": "POST",
    "guaranteedTargetAmount": False,
    "guaranteedTargetAmountAllowed": False,
    "id": "f6a8ed80-c5f1-4066-8399-40292c9363a0",
    "notices": [],
    "payOut": "BANK_TRANSFER",
    "paymentOptions": [
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 0.59,
                "priceSetId": 384,
                "total": 1.99,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0221,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "DEBIT",
            "payInProduct": "FAST",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 1.99, "currency": "GBP", "label": "1.99 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 1.99, "currency": "GBP", "label": "1.99 GBP"},
                },
            },
            "sourceAmount": 89.88,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 2.04,
                "priceSetId": 384,
                "total": 3.44,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0377,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "CREDIT",
            "payInProduct": "FAST",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 3.44, "currency": "GBP", "label": "3.44 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 3.44, "currency": "GBP", "label": "3.44 GBP"},
                },
            },
            "sourceAmount": 91.33,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 0.0,
                "priceSetId": 384,
                "total": 1.4,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0157,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "BANK_TRANSFER",
            "payInProduct": "CHEAP",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 1.4, "currency": "GBP", "label": "1.40 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 1.4, "currency": "GBP", "label": "1.40 GBP"},
                },
            },
            "sourceAmount": 89.29,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 0.0,
                "priceSetId": 384,
                "total": 1.4,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0157,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "PISP",
            "payInProduct": "CHEAP",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 1.4, "currency": "GBP", "label": "1.40 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 1.4, "currency": "GBP", "label": "1.40 GBP"},
                },
            },
            "sourceAmount": 89.29,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-02T17:30:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 0.0,
                "priceSetId": 384,
                "total": 1.4,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0157,
            "formattedEstimatedDelivery": "by Thursday 2025",
            "payIn": "SWIFT",
            "payInProduct": "ADVANCED",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 1.4, "currency": "GBP", "label": "1.40 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 1.4, "currency": "GBP", "label": "1.40 GBP"},
                },
            },
            "sourceAmount": 89.29,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 0.33,
                "priceSetId": 384,
                "total": 1.73,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0193,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "VISA_DEBIT_OR_PREPAID",
            "payInProduct": "FAST",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 1.73, "currency": "GBP", "label": "1.73 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 1.73, "currency": "GBP", "label": "1.73 GBP"},
                },
            },
            "sourceAmount": 89.62,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 4.89,
                "priceSetId": 384,
                "total": 6.29,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0668,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "INTERNATIONAL_DEBIT",
            "payInProduct": "FAST",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 6.29, "currency": "GBP", "label": "6.29 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 6.29, "currency": "GBP", "label": "6.29 GBP"},
                },
            },
            "sourceAmount": 94.18,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 3.66,
                "priceSetId": 384,
                "total": 5.06,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0544,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "MC_BUSINESS_CREDIT",
            "payInProduct": "FAST",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 5.06, "currency": "GBP", "label": "5.06 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 5.06, "currency": "GBP", "label": "5.06 GBP"},
                },
            },
            "sourceAmount": 92.95,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 0.59,
                "priceSetId": 384,
                "total": 1.99,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0221,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "MC_DEBIT_OR_PREPAID",
            "payInProduct": "FAST",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 1.99, "currency": "GBP", "label": "1.99 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 1.99, "currency": "GBP", "label": "1.99 GBP"},
                },
            },
            "sourceAmount": 89.88,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 1.13,
                "priceSetId": 384,
                "total": 2.53,
                "transferwise": 1.4,
            },
            "feePercentage": 0.028,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "MC_CREDIT",
            "payInProduct": "FAST",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 2.53, "currency": "GBP", "label": "2.53 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 2.53, "currency": "GBP", "label": "2.53 GBP"},
                },
            },
            "sourceAmount": 90.42,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 0.59,
                "priceSetId": 384,
                "total": 1.99,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0221,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "CARD",
            "payInProduct": "FAST",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 1.99, "currency": "GBP", "label": "1.99 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 1.99, "currency": "GBP", "label": "1.99 GBP"},
                },
            },
            "sourceAmount": 89.88,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 0.59,
                "priceSetId": 384,
                "total": 1.99,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0221,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "MAESTRO",
            "payInProduct": "FAST",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 1.99, "currency": "GBP", "label": "1.99 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 1.99, "currency": "GBP", "label": "1.99 GBP"},
                },
            },
            "sourceAmount": 89.88,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 2.92,
                "priceSetId": 384,
                "total": 4.32,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0468,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "MC_BUSINESS_DEBIT",
            "payInProduct": "FAST",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 4.32, "currency": "GBP", "label": "4.32 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 4.32, "currency": "GBP", "label": "4.32 GBP"},
                },
            },
            "sourceAmount": 92.21,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 3.66,
                "priceSetId": 384,
                "total": 5.06,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0544,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "VISA_BUSINESS_CREDIT",
            "payInProduct": "FAST",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 5.06, "currency": "GBP", "label": "5.06 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 5.06, "currency": "GBP", "label": "5.06 GBP"},
                },
            },
            "sourceAmount": 92.95,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 1.38,
                "priceSetId": 384,
                "total": 2.78,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0307,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "VISA_BUSINESS_DEBIT",
            "payInProduct": "FAST",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 2.78, "currency": "GBP", "label": "2.78 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 2.78, "currency": "GBP", "label": "2.78 GBP"},
                },
            },
            "sourceAmount": 90.67,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 4.89,
                "priceSetId": 384,
                "total": 6.29,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0668,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "INTERNATIONAL_CREDIT",
            "payInProduct": "FAST",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 6.29, "currency": "GBP", "label": "6.29 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 6.29, "currency": "GBP", "label": "6.29 GBP"},
                },
            },
            "sourceAmount": 94.18,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": False,
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 2.04,
                "priceSetId": 384,
                "total": 3.44,
                "transferwise": 1.4,
            },
            "feePercentage": 0.0377,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "VISA_CREDIT",
            "payInProduct": "FAST",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 3.44, "currency": "GBP", "label": "3.44 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 384,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 3.44, "currency": "GBP", "label": "3.44 GBP"},
                },
            },
            "sourceAmount": 91.33,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
        {
            "allowedProfileTypes": ["PERSONAL", "BUSINESS"],
            "disabled": True,
            "disabledReason": {
                "arguments": [],
                "code": "error.payInmethod.disabled",
                "message": "Open a multi currency "
                "account and add funds to "
                "instantly pay for your "
                "transfers.",
            },
            "estimatedDelivery": "2025-01-01T12:15:00Z",
            "estimatedDeliveryDelays": [],
            "fee": {
                "discount": 0,
                "partner": 0.0,
                "payIn": 0.0,
                "priceSetId": 381,
                "total": 1.22,
                "transferwise": 1.22,
            },
            "feePercentage": 0.0137,
            "formattedEstimatedDelivery": "by Wednesday 2025",
            "payIn": "BALANCE",
            "payInProduct": "BALANCE",
            "payOut": "BANK_TRANSFER",
            "price": {
                "items": [
                    {
                        "label": "Our fee",
                        "type": "TRANSFERWISE",
                        "value": {"amount": 1.22, "currency": "GBP", "label": "1.22 GBP"},
                    }
                ],
                "priceDecisionReferenceId": "5076f371-349c-43b4-e6dc-15a6453d39ce",
                "priceSetId": 381,
                "total": {
                    "label": "Total fees",
                    "type": "TOTAL",
                    "value": {"amount": 1.22, "currency": "GBP", "label": "1.22 GBP"},
                },
            },
            "sourceAmount": 89.11,
            "sourceCurrency": "GBP",
            "targetAmount": 110.0,
            "targetCurrency": "USD",
        },
    ],
    "providedAmountType": "TARGET",
    "rate": 1.25155,
    "rateExpirationTime": "2024-12-31T19:21:44Z",
    "rateTimestamp": "2024-12-31T17:20:14Z",
    "rateType": "FIXED",
    "sourceCurrency": "GBP",
    "status": "PENDING",
    "targetAmount": 110.0,
    "targetAmountAllowed": True,
    "targetCurrency": "USD",
    "transferFlowConfig": {
        "highAmount": {
            "offerPrefundingOption": False,
            "overLimitThroughCs": False,
            "overLimitThroughWiseAccount": False,
            "showEducationStep": False,
            "showFeePercentage": False,
            "trackAsHighAmountSender": False,
        }
    },
    "type": "REGULAR",
    "user": 12970746,
}

def test_parse_example():
    """Test the example response is without errors."""
    qr = QuoteResponse(**EXAMPLE_RESPONSE)
    assert qr.user == 12970746


def test_request_a_quote(sandbox):
    """We request a quote from the API."""
    q = QuoteRequest(sourceCurrency="GBP", targetCurrency="USD", sourceAmount=None, targetAmount=110)
    a = sandbox.quotes.example(q)
    assert QuoteResponse(**EXAMPLE_RESPONSE) == a