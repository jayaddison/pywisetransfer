"""Money Transfers

Get information about transfers.

See https://docs.wise.com/api-docs/api-reference/transfer

"""
from typing import Optional
from apiron import JsonEndpoint
from munch import munchify

from pywisetransfer import Client
from pywisetransfer.base import Base


class TransferService(Base):
    list = JsonEndpoint(path="/v1/transfers")
    get = JsonEndpoint(path="/v1/transfers/{transfer_id}")


class Transfer:
    def __init__(self, client: Client):
        self.service = TransferService(client=client)

    def list(
            self,
            profile_id: Optional[int]=None,
            status: Optional[str]=None,
            offset: Optional[int]=None,
            limit: Optional[int]=None,
            created_date_start: Optional[str]=None,
            created_date_end: Optional[str]=None,
            target_currency: Optional[str]=None,
            source_currency: Optional[str]=None
            ) -> list[dict]:
        """Get transfers for a profile.
        
        See https://docs.wise.com/api-docs/api-reference/transfer#list
        
        Args:
        
            profile_id: The optional profile id. Defaults to the current profile.
            
            status: Comma separated list of one or more status codes to filter transfers.
                See Track transfer status for complete list of statuses:
                https://api-docs.wise.com/api-docs/guides/send-money/tracking
            
            offset: Starting record number
            
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
            source_currency=source_currency
        )
        return munchify(self.service.list(params=params))

    def get(self, transfer_id: int|str) -> dict:
        return munchify(self.service.get(transfer_id=str(transfer_id)))

__all__ = ["Subscription"]