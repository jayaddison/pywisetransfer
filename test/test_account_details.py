import pytest
import responses

from pywisetransfer import Client


@pytest.fixture
def account_details_list_response():
    return [
        {
            "id": 123456789,
            "currency": {"code": "EUR", "name": "Euro"},
            "balanceId": -1,
            "title": "Your EUR account details",
            "subtitle": "IBAN and Swift/BIC",
            "status": "AVAILABLE",
            "deprecated": False,
            "migrated": False,
            "receiveOptions": [
                {
                    "type": "LOCAL",
                    "title": "Local",
                    "description": {
                        "title": "Your EUR account details",
                        "body": 'Receive from a bank in the Eurozone<a href="https://wise.com/help/17/borderless-account/2827505/how-do-i-use-my-eur-bank-details" rel="noopener" target="_blank">See how to use EUR account details</a>',
                        "cta": None,
                    },
                    "summaries": [
                        {
                            "type": "TIME",
                            "title": "Payments take up to 2 working days to arrive",
                            "description": None,
                        },
                        {
                            "type": "INFO",
                            "title": "SEPA includes countries in the EU and EEA",
                            "description": {
                                "title": "What’s SEPA?",
                                "body": '<p>SEPA stands for the Single Euro Payments Area. Within this area, cross-border euro payments must cost the same as a regular, local one. It’s EU law.</p><p>SEPA covers all the countries within the EU. It also includes other European countries like Monaco, Norway, and Switzerland.</p><p>So if your sender is sending from a euro bank account in one of these countries, they shouldn’t have to pay much — if anything — to send money to your EUR account details.</p><h5>Good to know</h5><ul><li>SEPA payments to your EUR account details usually take 1–2 working days.</li><li>Just because a country uses euros, doesn’t mean it’s in SEPA. Please check the list below if you’re unsure.</li></ul><p><a href="https://wise.com/help/articles/2968880/sepa-countries-and-ibans" rel="noopener" target="_blank">See the full list of SEPA countries</a></p>',
                                "cta": None,
                            },
                        },
                        {
                            "type": "SAFETY",
                            "title": "Learn how Wise keeps your money safe",
                            "description": {
                                "title": "How Wise keeps your money safe",
                                "body": '<ul><li>We follow strict regulations everywhere we work</li><li>We safeguard 100% of your cash</li><li>We work round the clock to keep your money protected</li></ul><p>Your Wise account, and the money in it, are managed and protected by Wise in your region.</p><p><a href="https://wise.com/help/articles/2949821/how-wise-keeps-your-money-safe?origin=topic-5U80whCL1cmJnbIVNGsm3h" rel="noopener" target="_blank">Learn more</a></p>',
                                "cta": None,
                            },
                        },
                    ],
                    "details": [
                        {
                            "type": "ACCOUNT_HOLDER",
                            "title": "Account holder",
                            "body": "Willis and Daughters 4056",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "SWIFT_CODE",
                            "title": "BIC",
                            "body": "TRWIBxxxxxx",
                            "description": {
                                "title": "What’s BIC?",
                                "body": "<p>A BIC code identifies banks and financial institutions globally. It says who and where they are — a sort of international bank code or ID.</p>",
                                "cta": None,
                            },
                            "hidden": False,
                        },
                        {
                            "type": "IBAN",
                            "title": "IBAN",
                            "body": "BE29 9670 xxxx xxxx",
                            "description": {
                                "title": "What is an IBAN?",
                                "body": '<p>IBAN stands for International Bank Account Number. Your EUR account details include a Belgian IBAN, which begins with BE.</p><p>You only have one Wise account, no matter how many account details you have. Your Wise account is managed and protected by Wise in your region. <a href="https://wise.com/help/articles/2897226" rel="noopener" target="_blank">Learn more.</a></p><p><b>Do you need an account number?</b></p><p>If your sender specifically asks for an account number, use: <strong>0000001</strong></p>',
                                "cta": {"label": "IBAN", "content": "BE29 9670 xxxx xxxx"},
                            },
                            "hidden": False,
                        },
                        {
                            "type": "BANK_NAME_AND_ADDRESS",
                            "title": "Bank name and address",
                            "body": "TransferWise Europe SA\nSquare de Meeûs 38 bte 40\nBrussels\n1000\nBelgium",
                            "description": {
                                "title": "Did they ask for a bank address?",
                                "body": "<p>Although Wise isn’t a bank, you can use these details if your sender needs a bank name and address and we’ll process the transfer.</p>",
                                "cta": None,
                            },
                            "hidden": False,
                        },
                    ],
                    "alert": None,
                    "shareText": None,
                },
                {
                    "type": "INTERNATIONAL",
                    "title": "Global · Swift",
                    "description": {
                        "title": "Your EUR account details",
                        "body": 'Receive from a bank outside the Eurozone<a href="https://wise.com/help/17/borderless-account/2827505/how-do-i-use-my-eur-bank-details" rel="noopener" target="_blank">See how to use EUR account details</a>',
                        "cta": None,
                    },
                    "summaries": [
                        {
                            "type": "TIME",
                            "title": "Payments take up to 5 working days to arrive",
                            "description": None,
                        },
                        {
                            "type": "SAFETY",
                            "title": "Learn how Wise keeps your money safe",
                            "description": {
                                "title": "How Wise keeps your money safe",
                                "body": '<ul><li>We follow strict regulations everywhere we work</li><li>We safeguard 100% of your cash</li><li>We work round the clock to keep your money protected</li></ul><p>Your Wise account, and the money in it, are managed and protected by Wise in your region.</p><p><a href="https://wise.com/help/articles/2949821/how-wise-keeps-your-money-safe?origin=topic-5U80whCL1cmJnbIVNGsm3h" rel="noopener" target="_blank">Learn more</a></p>',
                                "cta": None,
                            },
                        },
                    ],
                    "details": [
                        {
                            "type": "ACCOUNT_HOLDER",
                            "title": "Account holder",
                            "body": "Willis and Daughters 4056",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "SWIFT_CODE",
                            "title": "Swift/BIC",
                            "body": "TRWIBxxxxxx",
                            "description": {
                                "title": "What’s Swift/BIC?",
                                "body": "<p>A Swift/BIC code identifies banks and financial institutions globally. It says who and where they are — a sort of international bank code or ID.</p>",
                                "cta": None,
                            },
                            "hidden": False,
                        },
                        {
                            "type": "IBAN",
                            "title": "IBAN",
                            "body": "BE29 9670 xxxx xxxx",
                            "description": {
                                "title": "What is an IBAN?",
                                "body": '<p>IBAN stands for International Bank Account Number. Your EUR account details include a Belgian IBAN, which begins with BE.</p><p>You only have one Wise account, no matter how many account details you have. Your Wise account is managed and protected by Wise in your region. <a href="https://wise.com/help/articles/2897226" rel="noopener" target="_blank">Learn more.</a></p><p><b>Do you need an account number?</b></p><p>If your sender specifically asks for an account number, use: <strong>0000001</strong></p>',
                                "cta": {"label": "IBAN", "content": "BE29 9670 xxxx xxxx"},
                            },
                            "hidden": False,
                        },
                        {
                            "type": "BANK_NAME_AND_ADDRESS",
                            "title": "Bank name and address",
                            "body": "TransferWise Europe SA\nSquare de Meeûs 38 bte 40\nBrussels\n1000\nBelgium",
                            "description": {
                                "title": "Did they ask for a bank address?",
                                "body": "<p>Although Wise isn’t a bank, you can use these details if your sender needs a bank name and address and we’ll process the transfer.</p>",
                                "cta": None,
                            },
                            "hidden": False,
                        },
                    ],
                    "alert": None,
                    "shareText": None,
                },
            ],
            "bankFeatures": [
                {"key": "LOCAL_RECEIVE", "title": "Receive locally", "supported": True},
                {"key": "SWIFT", "title": "Receive internationally (Swift)", "supported": True},
                {"key": "DIRECT_DEBITS", "title": "Set up Direct Debits", "supported": True},
                {
                    "key": "PLATFORM_RECEIVE",
                    "title": "Receive from PayPal and Stripe",
                    "supported": True,
                },
            ],
        },
        {
            "id": None,
            "currency": {"code": "GBP", "name": "British pound (accepts US dollar)"},
            "balanceId": -1,
            "title": "Your GBP account details",
            "subtitle": "UK sort code, account number and IBAN to receive US dollars + 22 other currencies",
            "status": "AVAILABLE",
            "deprecated": False,
            "migrated": False,
            "receiveOptions": [
                {
                    "type": "LOCAL",
                    "title": "Local",
                    "description": {
                        "title": "Your GBP account details",
                        "body": 'Receive from a bank in the UK<a href="https://wise.com/help/17/borderless-account/2935927/how-do-i-use-my-gbp-bank-details" rel="noopener" target="_blank">See how to use GBP account details</a>',
                        "cta": None,
                    },
                    "summaries": [
                        {
                            "type": "TIME",
                            "title": "Payments take up to 1 working day to arrive",
                            "description": {
                                "title": "How long does it take to receive GBP?",
                                "body": "<p>Most GBP payments arrive in a few minutes. But sometimes, it can take longer — it depends on the kind of payment.</p><h5>Waiting for a payment?</h5><p>Ask your sender what kind of payment they sent you. The payment confirmation from their bank should show this.</p><p>Then, check the table below.</p><p>Here’s how long different payments take in the UK:</p><ul><li><strong>Faster payments</strong> – less than 2 hours.</li><li><strong>Bacs</strong> – 2–3 working days.</li><li><strong>CHAPS</strong> – 1 working day.</li></ul><p>If you’re waiting for longer than this, we can help. Just get in touch with a copy of the payment confirmation.</p>",
                                "cta": None,
                            },
                        }
                    ],
                    "details": [
                        {
                            "type": "ACCOUNT_HOLDER",
                            "title": "Account holder",
                            "body": "Willis and Daughters 4056",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "BANK_CODE",
                            "title": "Sort code",
                            "body": "23-1x-xx",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "ACCOUNT_NUMBER",
                            "title": "Account number",
                            "body": "1000xxxx",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "IBAN",
                            "title": "IBAN",
                            "body": "GB77 TRWI 2314 7010 0000 00",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "BANK_NAME_AND_ADDRESS",
                            "title": "Bank name and address",
                            "body": "TransferWise\n56 Shoreditch High Street\nLondon\nE1 6JJ\nUnited Kingdom",
                            "description": {
                                "title": "Did they ask for a bank address?",
                                "body": "<p>Although Wise isn’t a bank, you can use these details if your sender needs a bank name and address and we’ll process the transfer.</p><p>Our address changed in March 2025. Payments made using the previous address will still arrive.</p>",
                                "cta": None,
                            },
                            "hidden": False,
                        },
                    ],
                    "alert": None,
                    "shareText": None,
                },
                {
                    "type": "INTERNATIONAL",
                    "title": "Global · Swift",
                    "description": {
                        "title": "Your GBP account details",
                        "body": 'Receive from a bank outside the UK<a href="https://wise.com/help/17/borderless-account/2935927/how-do-i-use-my-gbp-bank-details" rel="noopener" target="_blank">See how to use GBP account details</a>',
                        "cta": None,
                    },
                    "summaries": [
                        {
                            "type": "TIME",
                            "title": "Payments take up to 5 working days to arrive",
                            "description": None,
                        },
                        {
                            "type": "INFO",
                            "title": "Receive payments in 22 other currencies with these details. Fees apply",
                            "description": {
                                "title": "Receive payments in 22 other currencies",
                                "body": '<p>Share these account details to receive payments in:</p><ul><li>AED, AUD, BGN, CAD, CHF, CNY, CZK, DKK, EUR, HKD, HUF, ILS, JPY, NOK, NZD, PLN, RON, SEK, SGD, UGX, USD and ZAR</li></ul><p>You can view the latest fees for receiving Swift payments on our <a href="https://wise.com/gb/pricing/receive" rel="noopener" target="_blank">pricing page</a>.</p><h5>Ask your sender to check about Swift fees</h5><p>Your sender’s bank may need to use <a href="https://wise.com/help/articles/3KEJruODkhi59TZbSxO2xn/what-are-swift-correspondent-fees" rel="noopener" target="_blank">correspondent banks</a> within the Swift network to complete the payment.</p><p>Correspondent banks can charge fees that are outside of our control and are deducted before the money reaches us. These fees are usually between 15 and 50 USD but can be higher. This means the amount that you receive can be less than was sent. </p><p>It’s best to ask your sender to check with their bank if there are any fees before they make the payment.</p>',
                                "cta": None,
                            },
                        },
                    ],
                    "details": [
                        {
                            "type": "ACCOUNT_HOLDER",
                            "title": "Account holder",
                            "body": "Willis and Daughters 4056",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "SWIFT_CODE",
                            "title": "Swift/BIC",
                            "body": "TRWIGB2L",
                            "description": {
                                "title": "What’s Swift/BIC?",
                                "body": "<p>A Swift/BIC code identifies banks and financial institutions globally. It says who and where they are — a sort of international bank code or ID.</p>",
                                "cta": None,
                            },
                            "hidden": False,
                        },
                        {
                            "type": "IBAN",
                            "title": "IBAN",
                            "body": "GB77 TRWI 2314 7010 0000 00",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "BANK_NAME_AND_ADDRESS",
                            "title": "Bank name and address",
                            "body": "TransferWise\n56 Shoreditch High Street\nLondon\nE1 6JJ\nUnited Kingdom",
                            "description": {
                                "title": "Did they ask for a bank address?",
                                "body": "<p>Although Wise isn’t a bank, you can use these details if your sender needs a bank name and address and we’ll process the transfer.</p><p>Our address changed in March 2025. Payments made using the previous address will still arrive.</p>",
                                "cta": None,
                            },
                            "hidden": False,
                        },
                    ],
                    "alert": None,
                    "shareText": None,
                },
            ],
            "bankFeatures": [
                {"key": "LOCAL_RECEIVE", "title": "Receive locally", "supported": True},
                {"key": "SWIFT", "title": "Receive internationally (Swift)", "supported": True},
                {"key": "DIRECT_DEBITS", "title": "Set up Direct Debits", "supported": True},
                {
                    "key": "PLATFORM_RECEIVE",
                    "title": "Receive from PayPal and Stripe",
                    "supported": True,
                },
            ],
        },
        {
            "id": None,
            "currency": {"code": "USD", "name": "US dollar"},
            "balanceId": -1,
            "title": "Your USD account details",
            "subtitle": "Routing number (ACH or ABA), account number and Swift/BIC",
            "status": "AVAILABLE",
            "deprecated": False,
            "migrated": False,
            "receiveOptions": [
                {
                    "type": "LOCAL",
                    "title": "Local",
                    "description": {
                        "title": "Your USD account details",
                        "body": "Receive from a bank in the USreceive-option.usd.description.body.links",
                        "cta": None,
                    },
                    "summaries": [
                        {
                            "type": "TIME",
                            "title": "Payments take up to 3 working days to arrive",
                            "description": None,
                        }
                    ],
                    "details": [
                        {
                            "type": "ACCOUNT_HOLDER",
                            "title": "Account holder",
                            "body": "Willis and Daughters 4056",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "ROUTING_NUMBER",
                            "title": "Wire routing number",
                            "body": "026073008",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "ACCOUNT_NUMBER",
                            "title": "Account number",
                            "body": "8xx00xxxxx",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "ACCOUNT_TYPE",
                            "title": "Account type",
                            "body": "Checking",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "BANK_NAME_AND_ADDRESS",
                            "title": "Bank name and address",
                            "body": "TransferWise\n19 W 24th Street\nNew York NY 10010\nUnited States",
                            "description": {
                                "title": "Did they ask for a bank address?",
                                "body": '<p>Community Federal Savings Bank is our partner bank in the US. If your sender asks for a bank name and address, give them these details and we’ll process the transfer.</p><p>Keep in mind that if you have questions or need help, you’ll need to contact us and not our partner bank. <a href="https://wise.com/help/articles/4ijaGT6BdeHNVjzbRip4gI" rel="noopener" target="_blank">Get help</a></p>',
                                "cta": None,
                            },
                            "hidden": False,
                        },
                    ],
                    "alert": None,
                    "shareText": None,
                },
                {
                    "type": "INTERNATIONAL",
                    "title": "Global · Swift",
                    "description": {
                        "title": "Your USD account details",
                        "body": "Receive from a bank outside the USreceive-option.usd.description.body.links",
                        "cta": None,
                    },
                    "summaries": [
                        {
                            "type": "TIME",
                            "title": "Payments take up to 5 working days to arrive",
                            "description": None,
                        }
                    ],
                    "details": [
                        {
                            "type": "ACCOUNT_HOLDER",
                            "title": "Account holder",
                            "body": "Willis and Daughters 4056",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "ROUTING_NUMBER",
                            "title": "Routing number",
                            "body": "026073008",
                            "description": {
                                "title": "Did they ask for a routing number?",
                                "body": "<p>A routing number is not required to add or receive USD from bank accounts outside the US. But if they specifically ask for a routing number, you can give them this:</p><p><strong>026073008</strong></p>",
                                "cta": {"label": "Routing number", "content": "026073008"},
                            },
                            "hidden": False,
                        },
                        {
                            "type": "SWIFT_CODE",
                            "title": "Swift/BIC",
                            "body": "CMFGxxxx",
                            "description": {
                                "title": "Swift/BIC",
                                "body": "<p>We’ll return payments from countries on this list to the sender. This can take 3–10 working days.</p><h5>Africa</h5><p>Burundi, Central African Republic, Chad, Democratic Republic of the Congo, Eritrea, Guinea-Bissau, Libya, Somalia, South Sudan, Sudan.</p><h5>Americas</h5><p>Cuba, Venezuela.</p><h5>Asia</h5><p>Democratic People’s Republic of Korea (North Korea). </p><h5>Europe</h5><p>Belarus, Crimea, Russian Federation, Serbia.</p><h5>Middle East</h5><p>Afghanistan, Iran, Iraq, Syria, Yemen.</p>",
                                "cta": {"label": "Swift/BIC", "content": "CMFGxxxx"},
                            },
                            "hidden": True,
                        },
                        {
                            "type": "ACCOUNT_NUMBER",
                            "title": "Account number",
                            "body": "8xx00xxxxx",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "BANK_NAME_AND_ADDRESS",
                            "title": "Bank name and address",
                            "body": "TransferWise\n19 W 24th Street\nNew York NY 10010\nUnited States",
                            "description": {
                                "title": "Did they ask for a bank address?",
                                "body": '<p>Community Federal Savings Bank is our partner bank in the US. If your sender asks for a bank name and address, give them these details and we’ll process the transfer.</p><p>Keep in mind that if you have questions or need help, you’ll need to contact us and not our partner bank. <a href="https://wise.com/help/articles/4ijaGT6BdeHNVjzbRip4gI" rel="noopener" target="_blank">Get help</a></p>',
                                "cta": None,
                            },
                            "hidden": False,
                        },
                    ],
                    "alert": None,
                    "shareText": None,
                },
            ],
            "bankFeatures": [
                {"key": "LOCAL_RECEIVE", "title": "Receive locally", "supported": True},
                {"key": "SWIFT", "title": "Receive internationally (Swift)", "supported": True},
                {"key": "DIRECT_DEBITS", "title": "Set up Direct Debits", "supported": True},
                {
                    "key": "PLATFORM_RECEIVE",
                    "title": "Receive from PayPal and Stripe",
                    "supported": True,
                },
            ],
        },
        {
            "id": None,
            "currency": {"code": "AUD", "name": "Australian dollar"},
            "balanceId": -1,
            "title": "Your AUD account details",
            "subtitle": "BSB code, account number and Swift/BIC",
            "status": "AVAILABLE",
            "deprecated": False,
            "migrated": False,
            "receiveOptions": [
                {
                    "type": "LOCAL",
                    "title": "Local",
                    "description": {
                        "title": "Your AUD account details",
                        "body": 'Receive from a bank in Australia<a href="https://wise.com/help/17/borderless-account/2879660/how-do-i-use-my-aud-bank-details" rel="noopener" target="_blank">See how to use AUD account details</a>',
                        "cta": None,
                    },
                    "summaries": [
                        {
                            "type": "TIME",
                            "title": "Payments take up to 1 working day to arrive",
                            "description": {
                                "title": "How long does it take to receive AUD?",
                                "body": "<p>Most AUD payments arrive in a few minutes. But sometimes, it can take longer — it depends on the kind of payment.</p><h5>Waiting for a payment?</h5><p>Ask your sender what kind of payment they sent you. The payment confirmation from their bank should show this.</p><p>Then, check the table below.</p><p>Here’s how long different payments take in Australia:</p><ul><li><strong>Instant-BSB, POLI, and Pay-ID payments</strong> – almost instantly.</li><li><strong>Traditional bank transfers (BECS)</strong> – 1 working day.</li></ul><p>If you’re waiting for longer than this, we can help. Just get in touch with a copy of the payment confirmation.",
                                "cta": None,
                            },
                        }
                    ],
                    "details": [
                        {
                            "type": "ACCOUNT_HOLDER",
                            "title": "Account holder",
                            "body": "Willis and Daughters 4056",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "BANK_CODE",
                            "title": "BSB code",
                            "body": "774xxx",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "ACCOUNT_NUMBER",
                            "title": "Account number",
                            "body": "6129xxxxx",
                            "description": None,
                            "hidden": False,
                        },
                    ],
                    "alert": None,
                    "shareText": None,
                },
                {
                    "type": "INTERNATIONAL",
                    "title": "Global · Swift",
                    "description": {
                        "title": "Your AUD account details",
                        "body": "Sorry, you can’t get account details to receive international AUD payments yet.",
                        "cta": None,
                    },
                    "summaries": [],
                    "details": [],
                    "alert": None,
                    "shareText": None,
                },
            ],
            "bankFeatures": [
                {"key": "LOCAL_RECEIVE", "title": "Receive locally", "supported": False},
                {"key": "SWIFT", "title": "Receive internationally (Swift)", "supported": True},
                {"key": "DIRECT_DEBITS", "title": "Set up Direct Debits", "supported": False},
                {
                    "key": "PLATFORM_RECEIVE",
                    "title": "Receive from PayPal and Stripe",
                    "supported": False,
                },
            ],
        },
        {
            "id": None,
            "currency": {"code": "NZD", "name": "New Zealand dollar"},
            "balanceId": -1,
            "title": "Your NZD account details",
            "subtitle": "Account number and Swift/BIC",
            "status": "AVAILABLE",
            "deprecated": False,
            "migrated": False,
            "receiveOptions": [
                {
                    "type": "LOCAL",
                    "title": "Local",
                    "description": {
                        "title": "Your NZD account details",
                        "body": 'Receive from a bank in New Zealand<a href="https://wise.com/help/17/borderless-account/2962566/how-do-i-use-my-nzd-bank-details" rel="noopener" target="_blank">See how to use NZD account details</a>',
                        "cta": None,
                    },
                    "summaries": [
                        {
                            "type": "INFO",
                            "title": "Direct Debits aren’t supported",
                            "description": {
                                "title": "We don’t support NZD Direct Debits yet",
                                "body": "<p>We hope to change this soon — and we’ll let you know when we do.</p><p>Until then, please don’t try to set up any Direct Debits with your NZD account details. The payment will be rejected and the merchant may charge you a fee.</p>",
                                "cta": None,
                            },
                        },
                        {
                            "type": "TIME",
                            "title": "Payments take up to 2 working days to arrive",
                            "description": None,
                        },
                    ],
                    "details": [
                        {
                            "type": "ACCOUNT_HOLDER",
                            "title": "Account holder",
                            "body": "Willis and Daughters 4056",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "ACCOUNT_NUMBER",
                            "title": "Account number",
                            "body": "02-1290-0xxxxxx-xxx",
                            "description": None,
                            "hidden": False,
                        },
                    ],
                    "alert": None,
                    "shareText": None,
                },
                {
                    "type": "INTERNATIONAL",
                    "title": "Global · Swift",
                    "description": {
                        "title": "Your NZD account details",
                        "body": "Sorry, you can’t get account details to receive international NZD payments yet.",
                        "cta": None,
                    },
                    "summaries": [],
                    "details": [],
                    "alert": None,
                    "shareText": None,
                },
            ],
            "bankFeatures": [
                {"key": "LOCAL_RECEIVE", "title": "Receive locally", "supported": True},
                {"key": "SWIFT", "title": "Receive internationally (Swift)", "supported": False},
                {"key": "DIRECT_DEBITS", "title": "Set up Direct Debits", "supported": False},
                {
                    "key": "PLATFORM_RECEIVE",
                    "title": "Receive from PayPal and Stripe",
                    "supported": False,
                },
            ],
        },
        {
            "id": None,
            "currency": {"code": "CAD", "name": "Canadian dollar"},
            "balanceId": -1,
            "title": "Your CAD account details",
            "subtitle": "Institution number, transit number, account number and Swift/BIC",
            "status": "AVAILABLE",
            "deprecated": False,
            "migrated": False,
            "receiveOptions": [
                {
                    "type": "LOCAL",
                    "title": "Local",
                    "description": {
                        "title": "Your CAD account details",
                        "body": 'Receive from a bank in Canada<a href="https://wise.com/help/articles/2978083/how-do-i-use-my-cad-bank-details" rel="noopener" target="_blank">See how to use CAD account details</a>',
                        "cta": None,
                    },
                    "summaries": [
                        {
                            "type": "INFO",
                            "title": "Domestic wire transfers and Online Bill Transfers (OBTs) are not yet supported",
                            "description": {
                                "title": "We support EFTs, Direct Deposits, Interac and Swift",
                                "body": '<p>You can always receive CAD into your local details via <strong>EFTs (electronic fund transfers)</strong> and <strong>Direct Deposits</strong>, or to your global details via <strong>Swift</strong>. <a href="https://wise.com/help/articles/2978083/how-do-i-use-my-cad-account-details" rel="noopener" target="_blank">Learn more here</a>.</p><p>You can also receive CAD to your email via <strong>Interac</strong>. <a href="https://wise.com/help/articles/7FVEZiHK6vnscBvc4eGWZF/how-do-i-receive-money-with-interac-autodeposit" rel="noopener" target="_blank">Learn more here</a>.</p><p>We don’t yet support the following payment methods:<ul><li>Domestic wire transfers</li><li>Online Bill Transfers (OBT)</li></ul></p><p>If a domestic wire is sent to this currency, it will be returned to the originating bank with $25 CAD deducted to cover return processing fees.</p>',
                                "cta": None,
                            },
                        },
                        {
                            "type": "TIME",
                            "title": "Payments take up to 2 working days to arrive",
                            "description": None,
                        },
                    ],
                    "details": [
                        {
                            "type": "ACCOUNT_HOLDER",
                            "title": "Account holder",
                            "body": "Willis and Daughters 4056",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "ROUTING_NUMBER",
                            "title": "Institution number",
                            "body": "6xx",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "ACCOUNT_NUMBER",
                            "title": "Account number",
                            "body": "200110xxxxxx",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "BANK_NAME_AND_ADDRESS",
                            "title": "Bank name and address",
                            "body": "Peoples Trust\n595 Burrard Street\nVancouver BC V7X 1L7\nCanada",
                            "description": {
                                "title": "Did they ask for a bank address?",
                                "body": '<p>Peoples Trust is our partner bank in Canada. If your sender asks for a bank name and address, give them these details and we’ll process the transfer.</p><p>Keep in mind that if you have questions or need help, you’ll need to contact us and not our partner bank. <a href="https://wise.com/help/articles/4ijaGT6BdeHNVjzbRip4gI" rel="noopener" target="_blank">Get help</a></p>',
                                "cta": None,
                            },
                            "hidden": False,
                        },
                    ],
                    "alert": None,
                    "shareText": None,
                },
                {
                    "type": "INTERNATIONAL",
                    "title": "Global · Swift",
                    "description": {
                        "title": "Your CAD account details",
                        "body": "Sorry, your Wise CAD account details do not yet support receiving CAD from banks via Swift transfers. If a Swift transfer is sent to this account, it will be returned to the originating bank with $50 CAD deducted to cover return processing fees.",
                        "cta": None,
                    },
                    "summaries": [],
                    "details": [],
                    "alert": None,
                    "shareText": None,
                },
            ],
            "bankFeatures": [
                {"key": "LOCAL_RECEIVE", "title": "Receive locally", "supported": True},
                {"key": "SWIFT", "title": "Receive internationally (Swift)", "supported": False},
                {"key": "DIRECT_DEBITS", "title": "Set up Direct Debits", "supported": True},
                {
                    "key": "PLATFORM_RECEIVE",
                    "title": "Receive from PayPal and Stripe",
                    "supported": False,
                },
            ],
        },
        {
            "id": None,
            "currency": {"code": "HUF", "name": "Hungarian forint"},
            "balanceId": -1,
            "title": "Your HUF account details",
            "subtitle": "Bank code, account number, IBAN and Swift/BIC",
            "status": "AVAILABLE",
            "deprecated": False,
            "migrated": False,
            "receiveOptions": [
                {
                    "type": "LOCAL",
                    "title": "Local",
                    "description": {
                        "title": "Your HUF account details",
                        "body": 'Receive from a bank in Hungary<a href="https://wise.com/help/articles/2978073/how-do-i-use-my-huf-bank-details" rel="noopener" target="_blank">See how to use HUF account details</a>',
                        "cta": None,
                    },
                    "summaries": [
                        {
                            "type": "TIME",
                            "title": "Payments take up to 1 working day to arrive",
                            "description": None,
                        }
                    ],
                    "details": [
                        {
                            "type": "ACCOUNT_HOLDER",
                            "title": "Account holder",
                            "body": "Willis and Daughters 4056",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "ACCOUNT_NUMBER",
                            "title": "Account number",
                            "body": "12600016-0000xxxx-xxxxxxxx",
                            "description": {
                                "title": "Did they ask for an IBAN?",
                                "body": "<p>For most payments in Hungary, you can use your account number. But if your sender specifically asked for an IBAN, you can give them this:</p><p><strong>HU68 1260 0016 0000 0000 0000 0000</strong></p><p>Just remember that this IBAN only works for HUF payments. So we recommend asking the sender which currency they’re sending you first.</p>",
                                "cta": {
                                    "label": "IBAN",
                                    "content": "HU68 1260 0016 0000 0000 0000 0000",
                                },
                            },
                            "hidden": False,
                        },
                        {
                            "type": "BANK_NAME_AND_ADDRESS",
                            "title": "Bank name and address",
                            "body": "TransferWise Europe SA\nSquare de Meeûs 38 bte 40\nBrussels\n1000\nBelgium",
                            "description": {
                                "title": "Did they ask for a bank address?",
                                "body": "<p>Although Wise isn’t a bank, you can use these details if your sender needs a bank name and address and we’ll process the transfer.</p>",
                                "cta": None,
                            },
                            "hidden": False,
                        },
                    ],
                    "alert": None,
                    "shareText": None,
                },
                {
                    "type": "INTERNATIONAL",
                    "title": "Global · Swift",
                    "description": {
                        "title": "Your HUF account details",
                        "body": 'Receive from a bank outside Hungary<a href="https://wise.com/help/articles/2978073/how-do-i-use-my-huf-bank-details" rel="noopener" target="_blank">See how to use HUF account details</a>',
                        "cta": None,
                    },
                    "summaries": [
                        {
                            "type": "TIME",
                            "title": "Payments take up to 5 working days to arrive",
                            "description": None,
                        },
                        {
                            "type": "FEE",
                            "title": "Fees can apply to receive Swift payments",
                            "description": {
                                "title": "What are the fees to receive HUF?",
                                "body": '<p>Your sender’s bank may need to use <a href="https://wise.com/help/articles/3KEJruODkhi59TZbSxO2xn/what-are-swift-correspondent-fees" rel="noopener" target="_blank">correspondent banks</a> within the Swift network to complete the payment.</p><p>Correspondent banks can charge fees that are outside of our control and are deducted before the money reaches us. These fees are usually between 15 and 50 USD but can be higher. This means the amount that you receive can be less than was sent.</p><p>It’s best to ask your sender to check with their bank if there are any fees before they make the payment.</p>',
                                "cta": None,
                            },
                        },
                    ],
                    "details": [
                        {
                            "type": "ACCOUNT_HOLDER",
                            "title": "Account holder",
                            "body": "Willis and Daughters 4056",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "SWIFT_CODE",
                            "title": "Swift/BIC",
                            "body": "TRWIBxxxxxx",
                            "description": {
                                "title": "What’s Swift/BIC?",
                                "body": "<p>A Swift/BIC code identifies banks and financial institutions globally. It says who and where they are — a sort of international bank code or ID.</p>",
                                "cta": {"label": "Swift/BIC", "content": "TRWIBxxxxxx"},
                            },
                            "hidden": False,
                        },
                        {
                            "type": "IBAN",
                            "title": "IBAN",
                            "body": "HU68 1260 0016 0000 0000 0000 0000",
                            "description": {
                                "title": "How to use your IBAN",
                                "body": '<p>Your IBAN is a code that helps banks identify your account for international payments. You can use your Hungarian IBAN to receive HUF payments.</p><h5>If you have problems using this IBAN</h5><p>Some banks may not be able to process payments using your Hungarian IBAN. If your sender has problems sending to this IBAN, you can receive HUF using GBP account details instead, and the payment will arrive as HUF into your account.</p><p><a href="https://wise.com/help/articles/2935927/how-do-i-use-my-gbp-account-details" rel="noopener" target="_blank">Learn more about using GBP account details</a></p>',
                                "cta": None,
                            },
                            "hidden": False,
                        },
                        {
                            "type": "BANK_NAME_AND_ADDRESS",
                            "title": "Bank name and address",
                            "body": "TransferWise Europe SA\nSquare de Meeûs 38 bte 40\nBrussels\n1000\nBelgium",
                            "description": {
                                "title": "Did they ask for a bank address?",
                                "body": "<p>Although Wise isn’t a bank, you can use these details if your sender needs a bank name and address and we’ll process the transfer.</p>",
                                "cta": None,
                            },
                            "hidden": False,
                        },
                    ],
                    "alert": None,
                    "shareText": None,
                },
            ],
            "bankFeatures": [
                {"key": "LOCAL_RECEIVE", "title": "Receive locally", "supported": True},
                {"key": "SWIFT", "title": "Receive internationally (Swift)", "supported": False},
                {"key": "DIRECT_DEBITS", "title": "Set up Direct Debits", "supported": False},
                {
                    "key": "PLATFORM_RECEIVE",
                    "title": "Receive from PayPal and Stripe",
                    "supported": False,
                },
            ],
        },
        {
            "id": None,
            "currency": {"code": "MYR", "name": "Malaysian ringgit"},
            "balanceId": -1,
            "title": "Your MYR account details",
            "subtitle": "Account number",
            "status": "AVAILABLE",
            "deprecated": False,
            "migrated": False,
            "receiveOptions": [
                {
                    "type": "LOCAL",
                    "title": "Local",
                    "description": {
                        "title": "Your MYR account details",
                        "body": 'Receive from a bank in Malaysia<a href="https://wise.com/help/articles/2lDYkmGHRiyfl1T8XKuahU/how-do-i-use-my-myr-account-details" rel="noopener" target="_blank">See how to use MYR account details</a>',
                        "cta": None,
                    },
                    "summaries": [
                        {
                            "type": "TIME",
                            "title": "Payments take up to 1 working day to arrive",
                            "description": None,
                        }
                    ],
                    "details": [
                        {
                            "type": "ACCOUNT_HOLDER",
                            "title": "Account holder",
                            "body": "Willis and Daughters 4056",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "PARTNER_BANK_NAME",
                            "title": "Partner bank name",
                            "body": "JPMorgan Chase Bank Berhad",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "ACCOUNT_NUMBER",
                            "title": "Account number",
                            "body": "3120000xxxxxxxx",
                            "description": None,
                            "hidden": False,
                        },
                    ],
                    "alert": None,
                    "shareText": None,
                },
                {
                    "type": "INTERNATIONAL",
                    "title": "Global · Swift",
                    "description": {
                        "title": "Your MYR account details",
                        "body": "Sorry, you can’t get account details to receive international MYR payments yet.",
                        "cta": None,
                    },
                    "summaries": [],
                    "details": [],
                    "alert": None,
                    "shareText": None,
                },
            ],
            "bankFeatures": [
                {"key": "LOCAL_RECEIVE", "title": "Receive locally", "supported": False},
                {"key": "SWIFT", "title": "Receive internationally (Swift)", "supported": False},
                {"key": "DIRECT_DEBITS", "title": "Set up Direct Debits", "supported": False},
                {
                    "key": "PLATFORM_RECEIVE",
                    "title": "Receive from PayPal and Stripe",
                    "supported": False,
                },
            ],
        },
        {
            "id": None,
            "currency": {"code": "RON", "name": "Romanian leu"},
            "balanceId": -1,
            "title": "Your RON account details",
            "subtitle": "Bank code, account number and IBAN",
            "status": "AVAILABLE",
            "deprecated": False,
            "migrated": False,
            "receiveOptions": [
                {
                    "type": "LOCAL",
                    "title": "Local",
                    "description": {
                        "title": "Your RON account details",
                        "body": 'Receive from a bank in Romania<a href="https://wise.com/help/17/borderless-account/2978062/how-do-i-use-my-ron-bank-details" rel="noopener" target="_blank">See how to use RON account details</a>',
                        "cta": None,
                    },
                    "summaries": [
                        {
                            "type": "TIME",
                            "title": "Payments take up to 1 working day to arrive",
                            "description": None,
                        }
                    ],
                    "details": [
                        {
                            "type": "ACCOUNT_HOLDER",
                            "title": "Account holder",
                            "body": "Willis and Daughters 4056",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "SWIFT_CODE",
                            "title": "Bank code",
                            "body": "BRELRxxxxxx",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "ACCOUNT_NUMBER",
                            "title": "Account number",
                            "body": "RO83 BREL 0005 xxxx xxxx xxxx",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "BANK_NAME_AND_ADDRESS",
                            "title": "Bank name and address",
                            "body": "Libra Internet Bank\nCalea Vitan Nr. 6-6A\nBucuresti\n031296\nRomania",
                            "description": {
                                "title": "Did they ask for a bank address?",
                                "body": '<p>Libra Internet Bank is our partner bank in Romania. If your sender asks for a bank name and address, give them these details and we’ll process the transfer.</p><p>Keep in mind that if you have questions or need help, you’ll need to contact us and not our partner bank. <a href="https://wise.com/help/articles/4ijaGT6BdeHNVjzbRip4gI" rel="noopener" target="_blank">Get help</a></p>',
                                "cta": None,
                            },
                            "hidden": False,
                        },
                    ],
                    "alert": None,
                    "shareText": None,
                },
                {
                    "type": "INTERNATIONAL",
                    "title": "Global · Swift",
                    "description": {
                        "title": "Your Currency(code=RON, name=Romanian leu) account details",
                        "body": "Use your Global Swift GBP details to receive RON from outside Romania.",
                        "cta": None,
                    },
                    "summaries": [],
                    "details": [],
                    "alert": None,
                    "shareText": None,
                },
            ],
            "bankFeatures": [
                {"key": "LOCAL_RECEIVE", "title": "Receive locally", "supported": True},
                {"key": "SWIFT", "title": "Receive internationally (Swift)", "supported": False},
                {"key": "DIRECT_DEBITS", "title": "Set up Direct Debits", "supported": False},
                {
                    "key": "PLATFORM_RECEIVE",
                    "title": "Receive from PayPal and Stripe",
                    "supported": False,
                },
            ],
        },
        {
            "id": None,
            "currency": {"code": "SGD", "name": "Singapore dollar"},
            "balanceId": -1,
            "title": "Your SGD account details",
            "subtitle": "Bank code, account number and Swift/BIC",
            "status": "AVAILABLE",
            "deprecated": False,
            "migrated": False,
            "receiveOptions": [
                {
                    "type": "LOCAL",
                    "title": "Local",
                    "description": {
                        "title": "Your SGD account details",
                        "body": 'Receive SGD payments instantly through the FAST network<a href="https://wise.com/help/17/borderless-account/2978053/how-do-i-use-my-sgd-bank-details" rel="noopener" target="_blank">See how to use SGD account details</a>',
                        "cta": None,
                    },
                    "summaries": [
                        {
                            "type": "TIME",
                            "title": "Payments take up to 1 working day to arrive",
                            "description": None,
                        },
                        {
                            "type": "LIMIT",
                            "title": "200,000 SGD limit per payment",
                            "description": None,
                        },
                    ],
                    "details": [
                        {
                            "type": "SUPPORTED_PAYMENT_NETWORK",
                            "title": "Payment network",
                            "body": "FAST",
                            "description": {
                                "title": "What is FAST?",
                                "body": "<p>FAST (Fast and Secure Transfer) is the most popular payment network in Singapore that allows payments to arrive instantly, 24/7.</p><h5>When to use your FAST account details</h5><ul><li>When you want to receive payments instantly— it’s speedy and available 24/7</li><li>To receive payments under 200,000 SGD</li></ul><p>If you want to receive payments from platforms like Google or Stripe, use your GIRO/MEPS account details instead.</p><h5>Useful to know</h5><p>You can only receive SGD from people or business that have a SGD bank account in Singapore.</p>",
                                "cta": None,
                            },
                            "hidden": False,
                        },
                        {
                            "type": "ACCOUNT_HOLDER",
                            "title": "Account holder",
                            "body": "Willis and Daughters 4056",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "BANK_NAME",
                            "title": "Bank name",
                            "body": "DBS Bank Ltd",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "BANK_CODE",
                            "title": "Bank code",
                            "body": "71xx",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "ACCOUNT_NUMBER",
                            "title": "Account number",
                            "body": "885-074-xxx-xxx",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "ADDRESS",
                            "title": "Wise’s address",
                            "body": "56 Shoreditch High Street\nLondon E1 6JJ",
                            "description": {
                                "title": "Did they ask for a bank address?",
                                "body": "<p>Although Wise isn’t a bank, you can use these details if your sender needs a bank name and address and we’ll process the transfer.</p>",
                                "cta": None,
                            },
                            "hidden": False,
                        },
                    ],
                    "alert": None,
                    "shareText": None,
                },
                {
                    "type": "INTERNATIONAL",
                    "title": "Global · Swift",
                    "description": {
                        "title": "Your SGD account details",
                        "body": "Sorry, you can’t get account details to receive international SGD payments yet.",
                        "cta": None,
                    },
                    "summaries": [],
                    "details": [],
                    "alert": None,
                    "shareText": None,
                },
            ],
            "bankFeatures": [
                {"key": "LOCAL_RECEIVE", "title": "Receive locally", "supported": True},
                {"key": "SWIFT", "title": "Receive internationally (Swift)", "supported": False},
                {"key": "DIRECT_DEBITS", "title": "Set up Direct Debits", "supported": False},
                {
                    "key": "PLATFORM_RECEIVE",
                    "title": "Receive from PayPal and Stripe",
                    "supported": False,
                },
            ],
        },
        {
            "id": None,
            "currency": {"code": "TRY", "name": "Turkish lira"},
            "balanceId": -1,
            "title": "Your TRY account details",
            "subtitle": "IBAN",
            "status": "AVAILABLE",
            "deprecated": False,
            "migrated": False,
            "receiveOptions": [
                {
                    "type": "LOCAL",
                    "title": "Local",
                    "description": {
                        "title": "Your TRY account details",
                        "body": 'Receive from a bank in Turkey<a href="https://wise.com/help/articles/2978080/how-do-i-use-my-try-bank-details" rel="noopener" target="_blank">See how to use TRY account details</a>',
                        "cta": None,
                    },
                    "summaries": [
                        {
                            "type": "TIME",
                            "title": "Payments take up to 1 working day to arrive",
                            "description": None,
                        }
                    ],
                    "details": [
                        {
                            "type": "ACCOUNT_HOLDER",
                            "title": "Account holder",
                            "body": "Willis and Daughters 4056",
                            "description": None,
                            "hidden": False,
                        },
                        {
                            "type": "IBAN",
                            "title": "IBAN",
                            "body": "TR29 0010 3000 0xxx xxxx xxxx xx",
                            "description": None,
                            "hidden": False,
                        },
                    ],
                    "alert": None,
                    "shareText": None,
                },
                {
                    "type": "INTERNATIONAL",
                    "title": "Global · Swift",
                    "description": {
                        "title": "Your TRY account details",
                        "body": "Sorry, you can’t get account details to receive international TRY payments yet.",
                        "cta": None,
                    },
                    "summaries": [],
                    "details": [],
                    "alert": None,
                    "shareText": None,
                },
            ],
            "bankFeatures": [
                {"key": "LOCAL_RECEIVE", "title": "Receive locally", "supported": True},
                {"key": "SWIFT", "title": "Receive internationally (Swift)", "supported": False},
                {"key": "DIRECT_DEBITS", "title": "Set up Direct Debits", "supported": False},
                {
                    "key": "PLATFORM_RECEIVE",
                    "title": "Receive from PayPal and Stripe",
                    "supported": False,
                },
            ],
        },
    ]


@responses.activate
def test_account_details_list(account_details_list_response):
    responses.add(
        responses.GET,
        "https://api.sandbox.transferwise.tech/v1/profiles/123456789/account-details",
        json=account_details_list_response,
    )

    endpoint = Client(api_key="test-key").account_details
    results = list(endpoint.list(profile_id=123456789))

    assert len(results) == 11
