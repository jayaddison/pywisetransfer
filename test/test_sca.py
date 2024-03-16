import pytest
import responses
from responses import matchers

from pywisetransfer import Client


@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as r:
        yield r


@pytest.fixture
def sca_challenge():
    return "7fa8c832-b8b5-4757-9c24-e952119999f2"


@pytest.fixture
def sca_challenge_signature():
    # echo -n 7fa8c832-b8b5-4757-9c24-e952119999f2|openssl sha256 -sign test-sca.pem | base64 -w 0
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
        "https://api.sandbox.transferwise.tech/v3/profiles/0/borderless-accounts/231/statement.json?"
        "currency=GBP&intervalStart=2021-12-28T00%3A00%3A00Z&intervalEnd=2021-12-29T00%3A00%3A00Z"
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
            "path": "/v3/profiles/0/borderless-accounts/1001/statement.json",
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
            "firstName": "Oliver",
            "lastName": "Wilson",
        },
        "issuer": {
            "name": "TransferWise Ltd.",
            "firstLine": "56 Shoreditch High Street",
            "city": "London",
            "postCode": "E1 6JJ",
            "stateCode": None,
            "country": "United Kingdom",
        },
        "bankDetails": [
            {
                "address": {
                    "firstLine": "Wise Payments Limited",
                    "secondLine": "56 Shoreditch High Street",
                    "postCode": "E1 6JJ",
                    "stateCode": None,
                    "city": "London",
                    "country": "United Kingdom",
                },
                "accountNumbers": [
                    {
                        "accountType": "Account number",
                        "accountNumber": "31926819",
                    },
                    {
                        "accountType": "IBAN",
                        "accountNumber": "GB29 NWBK 6016 1331 9268 19",
                    },
                ],
                "bankCodes": [{"scheme": "UK sort code", "value": "60-16-13"}],
                "deprecated": False,
            }
        ],
        "transactions": [],
        "endOfStatementBalance": {"value": 100.00, "currency": "GBP", "zero": False},
        "endOfStatementUnrealisedGainLoss": None,
        "query": {
            "intervalStart": "2021-12-28T00:00:00Z",
            "intervalEnd": "2021-12-29T00:00:00Z",
            "type": "COMPACT",
            "currency": "GBP",
            "profileId": 0,
            "timezone": "Z",
        },
        "request": {
            "id": "f847c6f9-691b-4213-b84d-2d60e018dc24",
            "creationTime": "2021-12-31T19:22:42.650161Z",
            "profileId": 0,
            "currency": "GBP",
            "balanceId": 121,
            "balanceName": None,
            "intervalStart": "2021-12-28T00:00:00Z",
            "intervalEnd": "2021-12-29T00:00:00Z",
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
        client.borderless_accounts.statement(
            0, 231, "GBP", "2021-12-28T00:00:00Z", "2021-12-29T00:00:00Z"
        )


def test_sca_statement_with_private_key(statement_forbidden, statement_authorised):
    client = Client(api_key="test-key", private_key_file="test/test-sca.pem")
    statement = client.borderless_accounts.statement(
        0, 231, "GBP", "2021-12-28T00:00:00Z", "2021-12-29T00:00:00Z"
    )
    assert "endOfStatementBalance" in statement
