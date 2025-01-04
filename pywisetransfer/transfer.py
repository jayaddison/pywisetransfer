"""Money Transfers

Get information about transfers.

See https://docs.wise.com/api-docs/api-reference/transfer

"""

from typing import List, Optional

from pywisetransfer.model.requirements import TransferRequirement, TransferRequirements
from pywisetransfer.model.transfer import TransferRequest, TransferResponse
from .endpoint import JsonEndpoint

from pywisetransfer import Client
from pywisetransfer.base import Base


class TransferService(Base):
    list = JsonEndpoint(path="/v1/transfers")
    get = JsonEndpoint(path="/v1/transfers/{transfer_id}")
    create = JsonEndpoint(default_method="POST", path="/v1/transfers")
    get_requirements = JsonEndpoint(default_method="POST", path="/v1/transfer-requirements")


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
    ) -> List[TransferResponse]:
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
        return [TransferResponse(**transfer) for transfer in self.service.list(params=params)]

    def get(self, transfer: int | str | TransferResponse) -> TransferResponse:
        response = self.service.get(transfer_id=transfer)
        return TransferResponse(**response)

    def create(self, transfer: TransferRequest) -> TransferResponse:
        """Create a new transfer.

        See https://docs.wise.com/api-docs/api-reference/transfer#create

        Check the requirements first with get_requirements(transfer).
        """
        response = self.service.create(json=transfer)
        return TransferResponse(**response)

    def get_requirements(self, transfer: TransferRequest) -> TransferRequirements:
        """Return a list of transfer requirements.

        See https://docs.wise.com/api-docs/api-reference/transfer#transfer-requirements
        """
        response = self.service.get_requirements(json=transfer)
        return TransferRequirements(TransferRequirement(**requirement) for requirement in response)


__all__ = ["Transfer"]
