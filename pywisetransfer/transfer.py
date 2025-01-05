"""Money Transfers

Get information about transfers.

See https://docs.wise.com/api-docs/api-reference/transfer

"""

from pprint import pprint
from typing import List, Optional

from apiron import Timeout

from pywisetransfer.model.payment import Payment, PaymentResponse
from pywisetransfer.model.profile import Profile
from pywisetransfer.model.requirements import TransferRequirement, TransferRequirements
from pywisetransfer.model.transfer import TransferRequest, TransferResponse
from .endpoint import JsonEndpoint, JsonEndpointWithSCA

from pywisetransfer import Client
from pywisetransfer.base import Base


class TransferService(Base):
    list = JsonEndpoint(path="/v1/transfers")
    get = JsonEndpoint(path="/v1/transfers/{transfer_id}")
    create = JsonEndpoint(default_method="POST", path="/v1/transfers")
    get_requirements = JsonEndpoint(default_method="POST", path="/v1/transfer-requirements")
    get_requirements.timeout_spec = Timeout(1, 10)  # requirements take a bit longer
    fund = JsonEndpointWithSCA(default_method="POST", path="/v3/profiles/{profile_id}/transfers/{transfer_id}/payments")

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
        # pprint(response)
        return TransferRequirements(TransferRequirement(**requirement) for requirement in response)

    def fund(self, transfer: TransferResponse|int, profile: int | Profile |None = None, payment:Payment|None=None) -> PaymentResponse:
        """Fund a transfer. (Pay for it)

        See https://docs.wise.com/api-docs/api-reference/transfer#fund
        
        This endpoint is SCA protected when it applies.
        If your profile is registered within the UK and/or EEA,
        SCA most likely applies to you. Please read more about implementing SCA below.
        
        You must pass a private key file to the client in order to use this functinality.
        
        Args:
            transfer: Transfer ID or Transfer object
            profile: Profile ID or Profile object
                If this is not provided, the business profile will be used if given
                by the transfer. If the transfer has no business profile information,
                we assume that the first personal profile is used.
            payment: Payment to perform
                This will be paid from your balance if no value is provided.
        """
        if not profile:
            if isinstance(transfer, TransferResponse):
                profile = transfer.business
                if profile is None:
                    profile = self.service.client.profiles.list().personal[0]
            else:
                raise ValueError("You must provide a profile")
        if payment is None:
            payment = Payment()
        response = self.service.fund(transfer_id=transfer, profile_id=profile, json=payment)
        # print(payment.model_dump_json())
        # pprint(response)
        return PaymentResponse(**response)

__all__ = ["Transfer"]
