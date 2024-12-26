"""Test the base methods."""

from pywisetransfer.base import Base

def test_kw_conversion():
    assert Base.get_params_for_endpoint(profile_id=1) == {"profileId": "1"}


def test_multiple_kw():
    assert Base.get_params_for_endpoint(
            profile_id=1,
            start=None,
            initialStart="asd-asd"
        ) == {
            "profileId": "1",
            "initialStart": "asd-asd"
        }
