"""Test the transfer endpoint."""


def test_list_and_limit_transfers(sandbox):
    """Test listing the transfers."""
    transfers = sandbox.transfers.list()
    assert len(transfers) == 3
    first_transfer = sandbox.transfers.list(limit=1)
    assert len(first_transfer) == 1
    next_transfer = sandbox.transfers.list(limit=1, offset=1)
    assert len(next_transfer) == 1
    assert next_transfer[0]["id"] != first_transfer[0]["id"]
    assert transfers[0]["id"] == first_transfer[0]["id"]
    assert transfers[1]["id"] == next_transfer[0]["id"]
    assert transfers[0] == first_transfer[0]
    assert transfers[1] == next_transfer[0]


def test_get_transfer(sandbox):
    """Test getting a transfer."""
    transfer = sandbox.transfers.get(transfer_id=777791907)
    assert transfer.id == 777791907
