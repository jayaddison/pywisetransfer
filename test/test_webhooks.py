from base64 import b64decode
import json

import pytest
from requests import Request

from pywisetransfer.webhooks import validate_request, verify_signature


@pytest.fixture
def valid_payload():
    return b'{"data":{"resource":{"id":0,"profile_id":0,"account_id":0,"type":"transfer"},"current_state":"processing","previous_state":"incoming_payment_waiting","occurred_at":"2022-02-23T19:22:53Z"},"subscription_id":"00000000-0000-0000-0000-000000000000","event_type":"transfers#state-change","schema_version":"2.0.0","sent_at":"2022-02-23T19:22:53Z"}'


@pytest.fixture
def corrupt_payload():
    return b'{"data":{"resource":{"id":0,"profile_id":0,"account_id":0,"type":"transfer"},"current_state":"processing","previous_state":"incoming_payment_waiting","occurred_at":"2022-02-23T19:22:53Z"},"subscription_id":"00000000-0000-0008-8000-000000000000","event_type":"transfers#state-change","schema_version":"2.0.0","sent_at":"2022-02-23T19:22:53Z"}'


@pytest.fixture
def valid_signature():
    return "EMRety5CM0VqStb6bIeB2DeQwdAO5Nm06ZSSGT0/8qW4+cbYDaPwFa5bL1Ylkn/E/JqKhZNtydeT0x+z+nkKCqlFx3Mt/K/WCSD9t+stoZa/Viv8GY8gVzt20A//2+mg0lqCdob5KFCBGHa7GRAwpO4WR5i5reBo17xubq6uVCB8/4hEUVDEstX1m32TU1OES1pFwWECCE/uFPoVJ+5h9BFqnVLSh2XnJde+9aHZ1N+nPBljZWCi9Z+iPpr1MFtHJdjGMPol8+i0VGzi02nhiHUNghmK4uIajB3rledPDZ0MgkQ3wfzJuzHcKGrb0iUMwAsOUNyEJT3b0/g4J7Ka+Q=="


@pytest.fixture
def corrupt_signature():
    return "EMRety5CM0VqStb6bIeB2DeQwdAO5Nm06ZSSGT0/8qW4+cbYDaPwFa5bL1Ylkn/E/JqKhZNtydeT1x+z+nkKCqlFx3Mt/K/WCSD9t+stoZa/Viv8GY8gVzt20A//2+mg0lqCdob5KFCBGHa7GRAwpO4WR5i5reBo17xubq6uVCB8/4hEUVDEstX1m32TU1OES1pFwWECCE/uFPoVJ+5h9BFqnVLSh2XnJde+9aHZ1N+nPBljZWCi9Z+iPpr1MFtHJdjGMPol8+i0VGzi02nhiHUNghmK4uIajB3rledPDZ0MgkQ3wfzJuzHcKGrb0iUMwAsOUNyEJT3b0/g4J7Ka+Q=="


def test_correct_signature(valid_payload, valid_signature):
    result = verify_signature(valid_payload, b64decode(valid_signature))
    assert result is True


def test_corrupt_payload(corrupt_payload, valid_signature):
    result = verify_signature(corrupt_payload, b64decode(valid_signature))
    assert result is False


def test_corrupt_signature(valid_payload, corrupt_signature):
    result = verify_signature(valid_payload, b64decode(corrupt_signature))
    assert result is False


@pytest.fixture
def valid_request(valid_payload, valid_signature):
    # Note: we construct an HTTP _client_ requests.Request object here; the
    # argument received at runtime will be the webserver's representation of
    # a request that it has received, and that interface may differ.
    return Request(
        method="GET",
        url="http://example.org",
        headers={
            "Content-Type": "application/json",
            "X-Signature-SHA256": valid_signature,
        },
        data=valid_payload,
        json=json.loads(valid_payload),
    )


def test_valid_request(valid_request):
    validate_request(valid_request)
