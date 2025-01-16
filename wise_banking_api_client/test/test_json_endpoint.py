"""This tests our JSON endpoint customizations."""

import pytest
from wise_banking_api_client import Client
from wise_banking_api_client.base import Base
from wise_banking_api_client.endpoint import JsonEndpoint, WiseAPIError
from wise_banking_api_client.model.quote import QuoteResponse, ExampleQuoteRequest


class MyService(Base):
    error_415 = JsonEndpoint(default_method="POST", path="/v0/415")


def test_error_description(client):
    """Make sure we see the error and it is nice!"""
    s = MyService(client=client)
    with pytest.raises(WiseAPIError) as e:
        s.error_415(data={})

    assert "Unsupported Media Type" in str(e.value)
    assert "/public/v3/quotes" in str(e.value)
    assert "Content-Type 'null' is not supported." in str(e.value)
    assert "415" in str(e.value)
