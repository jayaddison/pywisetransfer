"""Money Transfers

Get information about transfers.

See https://docs.wise.com/api-docs/api-reference/transfer

"""

from typing import Optional
from apiron import JsonEndpoint
from munch import munchify

from pywisetransfer import Client
from pywisetransfer.base import Base
from enum import Enum


class TransferStatus(str, Enum):
    """The transfer status

    See https://docs.wise.com/api-docs/guides/send-money/tracking

    You can use TransferStatusDescription to indicate the transfer status
    to the user.
    """

    incoming_payment_waiting = "incoming_payment_waiting"
    incoming_payment_initiated = "incoming_payment_initiated"
    processing = "processing"
    funds_converted = "funds_converted"
    outgoing_payment_sent = "outgoing_payment_sent"
    cancelled = "cancelled"
    funds_refunded = "funds_refunded"
    bounced_back = "bounced_back"
    charged_back = "charged_back"
    unknown = "unknown"


TransferStatusDescription = {
    TransferStatus.incoming_payment_waiting: "On its way to Wise",
    TransferStatus.incoming_payment_initiated: "On its way to Wise",
    TransferStatus.processing: "Processing",
    TransferStatus.funds_converted: "Processing",
    TransferStatus.outgoing_payment_sent: "Sent",
    TransferStatus.cancelled: "Cancelled",
    TransferStatus.funds_refunded: "Refunded",
    TransferStatus.bounced_back: "Bounced back",
    TransferStatus.charged_back: "Charged back",
    TransferStatus.unknown: "Unknown",
}


class TransferService(Base):
    list = JsonEndpoint(path="/v1/transfers")
    get = JsonEndpoint(path="/v1/transfers/{transfer_id}")


class Transfer:
    def __init__(self, client: Client):
        self.service = TransferService(client=client)

    def list(
        self,
        profile_id: Optional[int] = None,
        status: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        created_date_start: Optional[str] = None,
        created_date_end: Optional[str] = None,
        target_currency: Optional[str] = None,
        source_currency: Optional[str] = None,
    ) -> list[dict]:
        """Get transfers for a profile.

        See https://docs.wise.com/api-docs/api-reference/transfer#list

        Args:

            profile_id: The optional profile id. Defaults to the current profile.

            status: Comma separated list of one or more status codes to filter transfers.
                See Track transfer status for complete list of statuses:
                https://api-docs.wise.com/api-docs/guides/send-money/tracking

            offset: Starting record number (must be a multiple of limit)

            limit: Maximum number of records to be returned in response

            created_date_start: yyyy-mm-ddThh:mm:ss.sssZ
                Starting date to filter transfers, inclusive of the provided date.

            created_date_end: yyyy-mm-ddThh:mm:ss.sssZ
                Ending date to filter transfers, inclusive of the provided date.

            target_currency: Target currency code

            source_currency: Source currency code


        Returns:
            Returns an array of transfer objects, with or without an
            originator block depending on the type of each transfer.
            https://docs.wise.com/api-docs/api-reference/transfer#object
        """
        params = self.service.get_params_for_endpoint(
            profile_id=profile_id,
            status=status,
            offset=offset,
            limit=limit,
            created_date_start=created_date_start,
            created_date_end=created_date_end,
            target_currency=target_currency,
            source_currency=source_currency,
        )
        return munchify(self.service.list(params=params))

    def get(self, transfer_id: int | str) -> dict:
        return munchify(self.service.get(transfer_id=str(transfer_id)))


__all__ = ["Transfer", "TransferStatus", "TransferStatusDescription"]
