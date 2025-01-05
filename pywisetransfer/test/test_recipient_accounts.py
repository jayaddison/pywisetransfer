

from pywisetransfer.client import Client


def test_same_ids_returned_when_page_size_differs(client:Client):
    """The same accounts should be there."""
    ids_4 = [a.id for a in client.recipient_accounts.all(page_size=4)]
    ids_2 = [a.id for a in client.recipient_accounts.all(page_size=2)]
    assert ids_4 == ids_2

def test_get_recipient(client:Client):
    """Successfully get a recipient account."""
    client.recipient_accounts.get(700614969)
