"""pytest configuration

You can add responses by running this in your codebase:

    from pywisetransfer.test import record

    record()
    # do API requests
    record("name-of-endpoint")

"""

from typing import Generator
from unittest.mock import MagicMock
from munch import Munch
import pytest
from pywisetransfer import Client
from pywisetransfer.model.account import RecipientAccountRequirement, RecipientAccountResponse
from pywisetransfer.model.profile import Profile, Profiles
from pywisetransfer.model.quote import ExampleQuoteRequest, PaymentMethod, QuoteRequest
from pywisetransfer.model.recipient import Recipient
from pywisetransfer.model.recipient.details import RecipientDetails
from pywisetransfer.model.requirement_type import RequirementType
from pywisetransfer.test.record import TestClient
from pywisetransfer.model.currency import Currency, CurrencyCode


@pytest.fixture(scope="package")
def client() -> Generator[Client, None, None]:
    """We return a sandbox client and dispatch all requests.

    The responses are loaded from the RESPONSES directory.

    """
    client = TestClient()
    yield client
    client.stop()


@pytest.fixture(params=Currency.all_currencies())
def currency(request):
    return request.param


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add options to the pytest run."""
    parser.addoption(
        "--api_token", help="Run the tests on the real Wise Sandbox API.", default=None
    )


@pytest.fixture(scope="session")
def api_token(request: pytest.FixtureRequest) -> str:
    """Return the API token or skip the test."""
    api_token = request.config.getoption("--api_token")
    if api_token is None:
        pytest.skip("--api_token not provided, skipping tests.")
    return api_token


@pytest.fixture(scope="session")
def sandbox_client(api_token: str) -> Client:
    """The client communicating with the Wise Sandbox API."""
    return Client(api_key=api_token)


@pytest.fixture(scope="session")
def sandbox_profiles(sandbox_client: Client) -> Profiles:
    """Return the profiles from the sandbox."""
    return sandbox_client.profiles.list()


@pytest.fixture(scope="session")
def sandbox_currencies(sandbox_client: Client) -> list[Currency]:
    """Return the profiles from the sandbox."""
    return sandbox_client.currencies.list()


@pytest.fixture(scope="session")
def sandbox_personal_profile(sandbox_profiles: Profiles) -> Profile:
    """A personal profile."""
    if not sandbox_profiles.personal:
        pytest.skip("No personal profile found.")
    return sandbox_profiles.personal[0]


@pytest.fixture(scope="session")
def sandbox_business_profile(sandbox_profiles: Profiles) -> Profile:
    """A personal profile."""
    if not sandbox_profiles.business:
        pytest.skip("No business profile found.")
    return sandbox_profiles.business[0]


@pytest.fixture(scope="session")
def sandbox_personal_balances(
    sandbox_personal_profile: Profile, sandbox_client: Client
) -> list[Munch]:
    """The balances of a personal profile."""
    return sandbox_client.balances.list(profile=sandbox_personal_profile)


@pytest.fixture(scope="session")
def sandbox_requirements_gbp(sandbox_client: Client) -> list[RecipientAccountRequirement]:
    return sandbox_client.recipient_accounts.get_requirements_for_currency(
        source=Currency.GBP, target=Currency.GBP, source_amount=100
    )


@pytest.fixture(scope="session")
def example_quote_request() -> ExampleQuoteRequest:
    """An example quote request."""
    return ExampleQuoteRequest(
        sourceCurrency="GBP",
        targetCurrency="USD",
        sourceAmount=None,
        targetAmount=110,
    )


@pytest.fixture(scope="session")
def quote_request() -> QuoteRequest:
    """An example quote request."""
    return QuoteRequest(
        sourceCurrency="GBP",
        targetCurrency="USD",
        sourceAmount=None,
        targetAmount=110,
        targetAccount=None,
        payOut=PaymentMethod.BANK_TRANSFER,
        preferredPayIn=PaymentMethod.BANK_TRANSFER,
    )


@pytest.fixture(scope="session")
def sandbox_example_quote(
    sandbox_client: Client, example_quote_request: ExampleQuoteRequest
) -> QuoteRequest:
    """An example quote request."""
    return sandbox_client.quotes.example(example_quote_request)


@pytest.fixture
def mock():
    return MagicMock()


@pytest.fixture(scope="session")
def sandbox_email_recipient_request(sandbox_personal_profile: Profile)-> Recipient:
    """The data to request creating a new email recipient."""
    return Recipient(
        currency=CurrencyCode.EUR,
        type=RequirementType.email,
        profile=sandbox_personal_profile,
        accountHolderName="John Doe",
        ownedByCustomer=False,
        details=RecipientDetails(email="john@doe.com"),
    )


@pytest.fixture(scope="session")
def sandbox_email_recipient(sandbox_client: Client, sandbox_email_recipient_request:Recipient) -> RecipientAccountResponse:
    """Create an email recipient."""
    answer = sandbox_client.recipient_accounts.create_recipient(sandbox_email_recipient_request)
    return sandbox_client.recipient_accounts.get(answer)

    
