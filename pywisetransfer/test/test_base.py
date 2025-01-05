"""Test the base methods."""

from typing import Annotated
from uuid import UUID
from pydantic import PlainSerializer
from pytest import MonkeyPatch
from pywisetransfer.base import Base
from pywisetransfer.model.base import BaseModel
from pywisetransfer.model.currency import Currency
from pywisetransfer.model.quote import QuoteResponse


def test_kw_conversion():
    assert Base.get_params_for_endpoint(profile_id=1) == {"profileId": "1"}


def test_multiple_kw():
    assert Base.get_params_for_endpoint(profile_id=1, start=None, initialStart="asd-asd") == {
        "profileId": "1",
        "initialStart": "asd-asd",
    }


def test_bool():
    assert Base.get_params_for_endpoint(active=True) == {"active": "true"}
    assert Base.get_params_for_endpoint(active=False) == {"active": "false"}
    assert Base.get_params_for_endpoint(active=None) == {}


def test_list_of_string():
    assert Base.get_params_for_endpoint(type=["iban", "swift_code"]) == {"type": "iban,swift_code"}


def test_id():
    class X:
        id = 1223

    assert Base.get_params_for_endpoint(profile_id=X) == {"profileId": "1223"}


def test_code():
    assert Base.get_params_for_endpoint(currency=Currency.AED) == {"currency": "AED"}


def test_call_args_are_converted(client, monkeypatch: MonkeyPatch, mock, quote_request):
    """Check that we call the client with the correct arguments."""
    from apiron import client as apiron_client

    monkeypatch.setattr(apiron_client, "call", mock)
    example = QuoteResponse.model_example().model_dump()
    mock.return_value = example
    client.quotes.create(quote_request, profile="100")
    assert mock.call_count == 1
    call = mock.mock_calls[0]
    assert call.kwargs == dict(
        profile_id="100",
        json=quote_request.model_dump(),
    )


class ID(BaseModel):
    id: Annotated[UUID, PlainSerializer(str)]


def test_serialize_uid():
    m = ID(id=UUID("00000000-0000-0000-0000-000000000000"))
    assert m.model_dump() == {"id": "00000000-0000-0000-0000-000000000000"}
