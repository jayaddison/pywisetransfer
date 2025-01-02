"""Test the currencies and the endpoint."""

import pytest

from pywisetransfer.model.currency import Currency

def test_currency_has_code():
    assert Currency.AED.code == "AED"


def test_get_all_currencies():
    assert Currency.ARS in Currency.all_currencies()