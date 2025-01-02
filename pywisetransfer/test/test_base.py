"""Test the base methods."""

from pywisetransfer.base import Base
from pywisetransfer.model.currency import Currency


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
    assert Base.get_params_for_endpoint(type=["iban","swift_code"]) == {"type": "iban,swift_code"}


def test_id():
    class X:
        id = 1223
    assert Base.get_params_for_endpoint(profile_id=X) == {"profileId": "1223"}

def test_code():
    assert Base.get_params_for_endpoint(currency=Currency.AED) == {"currency": "AED"}