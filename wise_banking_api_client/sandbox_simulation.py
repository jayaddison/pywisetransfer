"""Money Transfers

Get information about transfers.

See https://docs.wise.com/api-docs/api-reference/transfer

"""

from typing import List, Optional

from wise_banking_api_client.model.requirements import TransferRequirement, TransferRequirements
from wise_banking_api_client.model.transfer import TransferRequest, TransferResponse, TransferStatus
from .endpoint import JsonEndpoint

from wise_banking_api_client import Client
from wise_banking_api_client.base import Base


class TransferSimulationService(Base):
    """Simulate transfers."""

    processing = JsonEndpoint(path="/v1/simulation/transfers/{transfer_id}/processing")
    funds_converted = JsonEndpoint(path="/v1/simulation/transfers/{transfer_id}/funds_converted")
    outgoing_payment_sent = JsonEndpoint(
        path="/v1/simulation/transfers/{transfer_id}/outgoing_payment_sent"
    )
    bounced_back = JsonEndpoint(path="/v1/simulation/transfers/{transfer_id}/bounced_back")
    funds_refunded = JsonEndpoint(path="/v1/simulation/transfers/{transfer_id}/funds_refunded")


class TransferSimulation:
    """Simulate transfers.

    See https://docs.wise.com/api-docs/api-reference/simulation
    """

    def __init__(self, client: Client):
        self.service = TransferSimulationService(client=client)

    def to_processing(self, transfer: TransferResponse | int) -> None:
        """Changes transfer status from incoming_payment_waiting to processing.

        Args:
            transfer: Transfer ID or Transfer object
        """
        self.service.processing(transfer_id=transfer)

    def to_funds_converted(self, transfer: TransferResponse | int) -> None:
        """Changes transfer status from processing to funds_converted.

        Please refer to our regional guides for any special regional requirements when simulating payments.
        https://docs.wise.com/api-docs/guides#regional-guides

        Args:
            transfer: Transfer ID or Transfer object
        """
        self.service.funds_converted(transfer_id=transfer)

    def to_outgoing_payment_sent(self, transfer: TransferResponse | int) -> None:
        """Changes transfer status from funds_converted to outgoing_payment_sent.

        Args:
            transfer: Transfer ID or Transfer object
        """
        self.service.outgoing_payment_sent(transfer_id=transfer)

    def to_bounced_back(self, transfer: TransferResponse | int) -> None:
        """Changes transfer status from outgoing_payment_sent to bounced_back.

        Args:
            transfer: Transfer ID or Transfer object
        """
        self.service.bounced_back(transfer_id=transfer)

    def to_funds_refunded(self, transfer: TransferResponse | int) -> None:
        """Changes transfer status from bounced_back to funds_refunded.

        Please note that this simulation will not trigger a refund webhook.

        Args:
            transfer: Transfer ID or Transfer object
        """
        self.service.funds_refunded(transfer_id=transfer)

    def to(self, status: TransferStatus, transfer: TransferResponse | int) -> None:
        """Change the status of the transfer inthe simulation.

        Args:
            status: Transfer status
            transfer: Transfer ID or Transfer object
        """
        func = getattr(self, f"to_{status}", self.to_unknown)
        func(transfer)

    def to_unknown(self, transfer: TransferResponse | int) -> None:
        """Cannot perform this action."""
        raise ValueError("The status of the transfer cannot be changed to this value.")


__all__ = ["TransferSimulation"]
