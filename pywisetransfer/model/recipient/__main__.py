from collections import defaultdict, namedtuple

from pydantic import Field
from pywisetransfer.model.account import RequiredFieldType
from pywisetransfer.test import TestClient
from pywisetransfer import Currency
from requests.exceptions import ConnectionError
from pathlib import Path

#   SchemaError: regex parse error:
# error: backreferences are not supported
BACK_REFERENCES = ["(?!", r"\1", r"\2", r"\3", r"\4", r"\5"]


def generate_recipient_details():
    HERE = Path(__file__).parent
    client = TestClient()
    select = defaultdict(set)
    TEXT = namedtuple("TEXT", ["start", "examples", "min_length", "max_length", "pattern"])
    text = dict()
    for currency in Currency.all_currencies():
        try:
            requirements = client.recipient_accounts.get_requirements_for_currency(
                source=currency, target=currency, source_amount=100
            )
        except ConnectionError:
            continue
        for requirement in requirements:
            for field in requirement.fields:
                for group in field.group:
                    key = group.key
                    added = False
                    if (
                        group.type in [RequiredFieldType.select, RequiredFieldType.radio]
                        and group.valuesAllowed
                    ):
                        for value in group.valuesAllowed:
                            select[key].add(value.key)
                        added = True
                    if (
                        not added
                    ):  # group.type == RequiredFieldType.text or group.type == RequiredFieldType.date:
                        start, examples, min_length, max_length, pattern = text.get(
                            key, TEXT("", set(), None, None, set())
                        )
                        if not start:
                            start = f"{group.key} : Optional[{'str' if group.type != RequiredFieldType.date else 'date'}] = Field("
                        if group.example:
                            examples.add(group.example)
                        if group.minLength and (min_length is None or group.minLength < min_length):
                            min_length = group.minLength
                        if group.maxLength and (max_length is None or group.maxLength > max_length):
                            max_length = group.maxLength
                        if group.validationRegexp:
                            pattern.add(
                                ".*"
                                if any(br in group.validationRegexp for br in BACK_REFERENCES)
                                else group.validationRegexp
                            )
                        text[key] = TEXT(start, examples, min_length, max_length, pattern)

    for key, value in text.copy().items():
        pattern = "(" + ")|(".join(sorted(value[4])) + ")" if value[4] else None
        examples = list(sorted(value[1])) if value[1] else None
        text[key] = (
            value[0]
            + f"examples={examples!r}, "
            + f"min_length={value[2]}, "
            + f"max_length={value[3]}, "
            + f"pattern={pattern!r}"
            + ", default=None)"
        )

    with (HERE / "literals.py").open("w") as f:
        print(
            """
# generated file
#    python -m pywisetransfer.model.recipient && black .

from typing import Literal

""",
            file=f,
        )
        literals = []
        for key, values in sorted(select.copy().items()):
            k = key.upper().replace(".", "_")
            print(f"{k}_VALUES = {list(sorted(values))}", file=f)
            print(f"{k} = Literal[*{k}_VALUES]", file=f)
            literals.append(k)
        literals = list(sorted(literals))
        print(f"__all__ = {literals}", file=f)

    with (HERE / "details.py").open("w") as f:
        print(
            f'''
# generated file
#    python -m pywisetransfer.model.recipient && black .

from .address import AddressDetails
from pydantic import BaseModel, Field
from typing import Literal, Optional
from datetime import date
from .literals import {', '.join(literals)}
        
class RecipientDetails(BaseModel):
    """The recipient details model.

    See https://docs.wise.com/api-docs/api-reference/recipient
    """
    dateOfBirth: Optional[date] = None
    address: Optional[AddressDetails] = None
    ''',
            file=f,
        )
        for key, values in sorted(select.items()):
            if not key.startswith("address"):
                print(f"    {key}: Optional[{key.upper().replace(".", "_")}] = None", file=f)
        for key, value in sorted(text.items()):
            if not key.startswith("address"):
                print(f"    {value}", file=f)
        print(
            """
              
__all__ = ["RecipientDetails"]
""",
            file=f,
        )

    with (HERE / "address.py").open("w") as f:
        print(
            """
# generated file
#    python -m pywisetransfer.model.recipient && black .

from pydantic import BaseModel, Field
from typing import Optional
from .literals import ADDRESS_COUNTRY
              
class AddressDetails(BaseModel):
""",
            file=f,
        )
        for key, value in sorted(text.items()):
            if key.startswith("address"):
                print(f"    {value[8:]}", file=f)
        for key, values in sorted(select.items()):
            if key.startswith("address"):
                print(f"    {key[8:]}: Optional[{key.upper().replace(".", "_")}] = None", file=f)
        print(
            """
__all__ = ["AddressDetails"]
""",
            file=f,
        )


if __name__ == "__main__":
    generate_recipient_details()
