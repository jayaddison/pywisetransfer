from pytransferwise import api_key, environment

from apiron import Service


class Base(Service):

    domain = (
        "https://api.transferwise.com"
        if environment == "live"
        else "https://api.sandbox.transferwise.tech"
    )
    required_headers = {"Authorization": f"Bearer {api_key}"}
