"""Command line interface for wise_banking_api_client."""

from typing import Any, Callable, Optional

try:
    import click
except ImportError:
    raise ImportError(
        "You need to install wisebanking_api_client[cli]:\n\n    pip install wisebanking_api_client[cli]"
    )
from pathlib import Path


HERE = Path(__file__).parent
LICENSE = (HERE / ".." / "LICENSE").read_text()


DEFAULT_PRIVATE_KEY = "wise.com.private.pem"
DEFAULT_PUBLIC_KEY = "wise.com.public.pem"


def opt_license(*param_decls: str, **kwargs: Any) -> Callable:
    """Show the license

    This is copied from the --help option.
    """

    def callback(
        ctx: click.Context, param: click.Parameter, value: bool
    ) -> None:  # noqa: FBT001, ARG001
        if not value or ctx.resilient_parsing:
            return
        click.echo(LICENSE)
        ctx.exit()

    if not param_decls:
        param_decls = ("--license",)

    kwargs.setdefault("is_flag", True)
    kwargs.setdefault("expose_value", False)
    kwargs.setdefault("is_eager", True)
    kwargs.setdefault("help", "Show the license and exit.")
    kwargs["callback"] = callback
    return click.option(*param_decls, **kwargs)


ARG_API_KEY = click.argument("api_key", envvar="WISE_API_KEY", required=True)
ARG_PRIVATE_KEY = click.argument(
    "private_key",
    envvar="WISE_PRIVATE_KEY",
    required=False,
    default=DEFAULT_PRIVATE_KEY,
    callback=lambda ctx, _, p: p if Path(p).exists() else None,
    expose_value=True,
)
ARG_ENV = click.argument(
    "env",
    envvar="WISE_ENV",
    required=True,
    default="sandbox,live",
    callback=lambda ctx, _, value: value.split(","),
    expose_value=True,
)


@click.group()
@opt_license()
@click.version_option()
def main():
    """General arguments are defined here.

    WISE_ENV or --env:

    \b
        The environment to use. Must be sandbox or live or a comma seperated list to use both. By default both or the first are used."

    WISE_API_KEY or --api-key:

    \b
        The API key to use.

    WISE_PRIVATE_KEY or --private-key:

    \b
        The private key to use.
        By default this is ./wise.com.private.pem
    """
    pass


@main.command()
@ARG_PRIVATE_KEY
@click.argument("public_key", type=click.Path(), default=DEFAULT_PUBLIC_KEY)
def new_key(private_key: Path, public_key: Path):
    """Generate a new key.

    If the private key exists, it will not be created again.
    Instead, only the public key will be generated.

    By default, this will generate these files:

    \b
        ./wise.com.private.pem
        ./wise.com.public.pem

    Read more here:

    \b
    https://docs.wise.com/api-docs/features/strong-customer-authentication-2fa/personal-token-sca

    """
    from wise_banking_api_client.client import generate_key_pair

    generate_key_pair(private_key=private_key, public_key=public_key)
    click.echo(f"private key: {private_key}")
    click.echo(f"public  key: {public_key}")
    click.echo(
        "You can now upload the public key to https://wise.com or "
        "https://sandbox.transferwise.tech."
    )


@main.command()
@ARG_API_KEY
@ARG_ENV
@ARG_PRIVATE_KEY
def check(api_key: str, private_key: Optional[Path], env: list[str]):
    """Check that we can access the API."""
    from wise_banking_api_client.client import Client, Environment

    for environment in env:
        if environment not in Environment:
            raise ValueError(f"Environment must be sandbox or live, not {environment}")
        client = Client(api_key=api_key, environment=environment, private_key_file=private_key)
        permissions = []
        if client.can_read():
            permissions.append("read")
            if client.can_write():
                permissions.append("write")
                if client.can_sca():
                    permissions.append("sca")
        if not permissions:
            permissions = ["none"]
        click.echo(f"Permissions on {environment}: {"+".join(permissions)}")


if __name__ == "__main__":
    main()
