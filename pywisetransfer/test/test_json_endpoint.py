"""This tests our JSON endpoint customizations."""

import pytest
from pywisetransfer import Client
from pywisetransfer.base import Base
from pywisetransfer.endpoint import JsonEndpoint, WiseAPIError
from pywisetransfer.model.quote import QuoteResponse, QuoteRequest


class MyService(Base):
    error_415 = JsonEndpoint(default_method="POST", path="/v0/415")

def test_error_description(sandbox):
    """Make sure we see the error and it is nice!"""
    s = MyService(client=sandbox)
    with pytest.raises(WiseAPIError) as e:
        s.error_415(data={})
    
    assert "Unsupported Media Type" in str(e.value)
    assert "/public/v3/quotes" in str(e.value)
    assert "Content-Type 'null' is not supported." in str(e.value)
    assert "415" in str(e.value)
