"""Test all the examples."""

from datetime import date
from enum import Enum
from pathlib import Path
from typing import Type

import pytest
import wise_banking_api_client.model
from importlib import import_module

from wise_banking_api_client.model.base import BaseModel
import wise_banking_api_client
import wise_banking_api_client.model
from wise_banking_api_client.model.enum import StrEnum
from wise_banking_api_client.model.recipient.details import RecipientDetails

MODELS_WITH_EXAMPLES = set()
MODELS = set()
ENUMS = set()

MODEL_DIR = Path(wise_banking_api_client.model.__file__).parent
for file in MODEL_DIR.iterdir():
    if file.suffix.lower() == ".py":
        module = import_module(f"wise_banking_api_client.model.{file.stem}")
        print("collecting models from", module.__name__)
        for cls in module.__dict__.values():
            if isinstance(cls, type) and issubclass(cls, BaseModel):
                if cls.EXAMPLE_JSON != BaseModel.EXAMPLE_JSON:
                    MODELS_WITH_EXAMPLES.add(cls)
                MODELS.add(cls)
            elif isinstance(cls, type) and issubclass(cls, Enum):
                ENUMS.add(cls)

ENUMS.remove(Enum)
ENUMS.remove(StrEnum)
MODELS.remove(BaseModel)

UPDATED_MODELS_ALL = list(
    sorted(set([cls.__name__ for cls in MODELS | ENUMS] + wise_banking_api_client.model.__all__))
)
UPDATED_PACKAGE_ALL = list(
    sorted(set([cls.__name__ for cls in MODELS | ENUMS] + wise_banking_api_client.__all__))
)


@pytest.mark.parametrize("model_class", MODELS_WITH_EXAMPLES)
def test_parse_requests(model_class: Type[BaseModel]):
    """Check that the example can be parsed."""
    print("checking", import_module(model_class.__module__).__file__, "->", model_class.__name__)
    e = model_class.model_example()
    json: str = "\n    " + "\n    ".join(e.model_dump_json(indent=4).splitlines()) + "\n    "
    print("EXAMPLE_JSON: ", repr(e.EXAMPLE_JSON))
    print("EXPECTED JSON:", repr(json))
    print("--------------------")
    print("Expected:")
    print(
        '''
    EXAMPLE_JSON: ClassVar[
        str
    ] = """'''
        + json
        + '"""'
    )
    print()
    print("in", import_module(model_class.__module__).__file__, "->", model_class.__name__)
    assert e.EXAMPLE_JSON == json


@pytest.mark.parametrize("model_class", MODELS | ENUMS)
def test_model_is_in_all(model_class: type):
    """Make sure we export all the models."""
    module = import_module(model_class.__module__)
    assert model_class.__name__ in module.__all__


@pytest.mark.parametrize("depth", ["", ".model"])
@pytest.mark.parametrize("model_class", MODELS | ENUMS)
def test_export_all(model_class: type, depth: str):
    """Make sure we find those models in the base."""
    package_root = import_module(model_class.__module__.split(".")[0] + depth)
    print("Expected in", package_root.__file__, ":")
    print("__all__ =", (UPDATED_PACKAGE_ALL if depth == "" else UPDATED_MODELS_ALL))
    assert model_class.__name__ in package_root.__all__
    assert getattr(package_root, model_class.__name__) is model_class


def test_is_included():
    from wise_banking_api_client.model import TransferRequest

    assert TransferRequest in MODELS
    assert TransferRequest in MODELS_WITH_EXAMPLES


# @pytest.mark.parametrize("dt", ["1990-10-12", "1970-01-01"])
# def test_details_with_date(dt: str):
#     r = RecipientDetails.model_validate_json(f'{{"dateOfBirth":"{dt}"}}')
#     assert r.dateOfBirth == date(*map(lambda x: int(x.lstrip("0")), dt.split("-")))


# def test_date_to_string():
#     r = RecipientDetails()
#     r.dateOfBirth = date(1990, 10, 1)
#     d = r.model_dump()
#     print(d)
#     assert d["dateOfBirth"] == "1990-10-01"
