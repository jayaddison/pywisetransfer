import os
import pytest
import responses
from responses import matchers

from wise_banking_api_client import Client
from wise_banking_api_client.client import DEFAULT_PRIVATE_KEY


@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as r:
        yield r


@pytest.fixture
def sca_challenge():
    return "7fa8c832-b8b5-4757-9c24-e952119999f2"


@pytest.fixture
def sca_challenge_signature():
    # echo -n 7fa8c832-b8b5-4757-9c24-e952119999f2|openssl sha256 -sign private.pem | base64 -w 0
    return (
        "H4AmLxMBsJ08oF80anN/Co4MbfhP6BQP0f43xVlmUP2a3W2n63izw3QNHciWxiTe3udX8RD7hE6p+p5s"
        "GRgIRbBgu1l53o021+i2GY0HhXiVc78HPjIpLepJbI4DqetdWXho6RAUppRj57knGn1iCrh/w+4VMWA8"
        "MdmNIzWV0gTE7nI+RzW2skhEPSshkZoz/oWX6blOzrMSIl5ujz7ji7uTnTJDXEtGst6XhB52L77NWo38"
        "6QrFWwbvQB/X9n20ZVaU3jP194qKNtytqneAs37hdhWak9+Ul5/G2gDLKUUUhYO0dFXkljwSJ4ArZtKI"
        "PXY0KPupPCkCimS7fCnWmQ=="
    )


@pytest.fixture
def statement_url():
    return (
        "https://api.sandbox.transferwise.tech/v1/profiles/0/balance-statements/231/statement.json?"
        "currency=GBP&intervalStart=2018-03-01T00%3A00%3A00Z&intervalEnd=2018-04-30T23%3A59%3A59.999Z&"
        "type=FLAT"
    )


@pytest.fixture
def statement_forbidden(statement_url, sca_challenge, mocked_responses):
    url, _, qs = statement_url.partition("?")
    mocked_responses.add(
        responses.GET,
        url,
        match=[
            matchers.query_string_matcher(qs),
        ],
        status=403,
        json={
            "timestamp": "2021-12-31T01:23:12.965+00:00",
            "status": 403,
            "error": "Forbidden",
            "message": "You are forbidden to send this request",
            "path": "/v1/profiles/0/balance-statements/1001/statement.json",
        },
        headers={
            "X-2FA-Approval-Result": "REJECTED",
            "X-2FA-Approval": sca_challenge,
        },
    )


@pytest.fixture
def statement_success():
    return {
        "accountHolder": {
            "type": "PERSONAL",
            "address": {
                "addressFirstLine": "Veerenni 24",
                "city": "Tallinn",
                "postCode": "12112",
                "stateCode": "",
                "countryName": "Estonia",
            },
            "firstName": "Oliver",
            "lastName": "Wilson",
        },
        "issuer": {
            "name": "TransferWise Ltd.",
            "firstLine": "56 Shoreditch High Street",
            "city": "London",
            "postCode": "E1 6JJ",
            "stateCode": "",
            "country": "United Kingdom",
        },
        "bankDetails": None,
        "transactions": [
            {
                "type": "DEBIT",
                "date": "2018-04-30T08:47:05.832Z",
                "amount": {"value": -7.76, "currency": "EUR"},
                "totalFees": {"value": 0.04, "currency": "EUR"},
                "details": {
                    "type": "CARD",
                    "description": "Card transaction of 6.80 GBP issued by Tfl.gov.uk/cp TFL TRAVEL CH",
                    "amount": {"value": 6.8, "currency": "GBP"},
                    "category": "Transportation Suburban and Loca",
                    "merchant": {
                        "name": "Tfl.gov.uk/cp",
                        "firstLine": None,
                        "postCode": "SW1H 0TL  ",
                        "city": "TFL TRAVEL CH",
                        "state": "   ",
                        "country": "GB",
                        "category": "Transportation Suburban and Loca",
                    },
                },
                "exchangeDetails": {
                    "forAmount": {"value": 6.8, "currency": "GBP"},
                    "rate": None,
                },
                "runningBalance": {"value": 16.01, "currency": "EUR"},
                "referenceNumber": "CARD-249281",
            },
            {
                "type": "CREDIT",
                "date": "2018-04-17T07:47:00.227Z",
                "amount": {"value": 200, "currency": "EUR"},
                "totalFees": {"value": 0, "currency": "EUR"},
                "details": {
                    "type": "DEPOSIT",
                    "description": "Received money from HEIN LAURI with reference SVWZ+topup card",
                    "senderName": "HEIN LAURI",
                    "senderAccount": "EE76 1700 0170 0049 6704 ",
                    "paymentReference": "SVWZ+topup card",
                },
                "exchangeDetails": None,
                "runningBalance": {"value": 207.69, "currency": "EUR"},
                "referenceNumber": "TRANSFER-34188888",
            },
            {
                "type": "CREDIT",
                "date": "2018-04-10T05:58:34.681Z",
                "amount": {"value": 9.94, "currency": "EUR"},
                "totalFees": {"value": 0, "currency": "EUR"},
                "details": {
                    "type": "CONVERSION",
                    "description": "Converted 8.69 GBP to 9.94 EUR",
                    "sourceAmount": {"value": 8.69, "currency": "GBP"},
                    "targetAmount": {"value": 9.94, "currency": "EUR"},
                    "fee": {"value": 0.03, "currency": "GBP"},
                    "rate": 1.147806,
                },
                "exchangeDetails": None,
                "runningBalance": {"value": 9.94, "currency": "EUR"},
                "referenceNumber": "CONVERSION-1511237",
            },
        ],
        "endOfStatementBalance": {"value": 9.94, "currency": "EUR"},
        "query": {
            "intervalStart": "2018-03-01T00:00:00Z",
            "intervalEnd": "2018-04-30T23:59:59.999Z",
            "currency": "EUR",
            "accountId": 64,
        },
    }


@pytest.fixture
def statement_authorised(
    statement_url,
    statement_success,
    sca_challenge,
    sca_challenge_signature,
    mocked_responses,
):
    url, _, qs = statement_url.partition("?")
    mocked_responses.add(
        responses.GET,
        url,
        match=[
            matchers.query_string_matcher(qs),
            matchers.header_matcher(
                {
                    "X-Signature": sca_challenge_signature,
                    "X-2FA-Approval": sca_challenge,
                }
            ),
        ],
        status=200,
        json=statement_success,
        headers={
            "X-2FA-Approval-Result": "APPROVED",
        },
    )


def test_sca_statement_without_private_key(statement_forbidden):
    client = Client(api_key="test-key")
    with pytest.raises(Exception, match="Please provide.*private_key.*"):
        client.balance_statements.statement(
            profile_id=0,
            balance_id=231,
            currency="GBP",
            interval_start="2018-03-01T00:00:00Z",
            interval_end="2018-04-30T23:59:59.999Z",
            type="FLAT",
        )


def test_sca_statement_with_private_key(statement_forbidden, statement_authorised):
    client = Client(api_key="test-key", private_key_file=DEFAULT_PRIVATE_KEY)
    statement = client.balance_statements.statement(
        profile_id=0,
        balance_id=231,
        currency="GBP",
        interval_start="2018-03-01T00:00:00Z",
        interval_end="2018-04-30T23:59:59.999Z",
        type="FLAT",
    )
    assert "endOfStatementBalance" in statement
