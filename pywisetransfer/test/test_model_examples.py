"""Test all the examples."""

from enum import Enum
from pathlib import Path
from typing import Type

import pytest
import pywisetransfer.model
from importlib import import_module

from pywisetransfer.model.base import BaseModel
import pywisetransfer
import pywisetransfer.model

MODELS_WITH_EXAMPLES = []
MODELS = []
ENUMS = []

MODEL_DIR = Path(pywisetransfer.model.__file__).parent
for file in MODEL_DIR.iterdir():
    if file.suffix.lower() == ".py":
        module = import_module(f"pywisetransfer.model.{file.stem}")
        for cls in module.__dict__.values():
            if isinstance(cls, type) and issubclass(cls, BaseModel):
                if cls.EXAMPLE_JSON != BaseModel.EXAMPLE_JSON:
                    MODELS_WITH_EXAMPLES.append(cls)
                MODELS.append(cls)
            elif isinstance(cls, type) and issubclass(cls, Enum):
                ENUMS.append(cls)

ENUMS.remove(Enum)

UPDATED_MODELS_ALL = list(sorted(set([cls.__name__ for cls in MODELS + ENUMS] + pywisetransfer.model.__all__)))
UPDATED_PACKAGE_ALL = list(sorted(set([cls.__name__ for cls in MODELS + ENUMS] + pywisetransfer.__all__)))


@pytest.mark.parametrize("model_class", MODELS_WITH_EXAMPLES)
def test_parse_requests(model_class: Type[BaseModel]):
    """Check that the example can be parsed."""
    print("checking", import_module(model_class.__module__).__file__, "->", model_class.__name__)
    e = model_class.example()
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


@pytest.mark.parametrize("model_class", MODELS + ENUMS)
def test_model_is_in_all(model_class: type):
    """Make sure we export all the models."""
    module = import_module(model_class.__module__)
    assert model_class.__name__ in module.__all__


@pytest.mark.parametrize("depth", ["", ".model"])
@pytest.mark.parametrize("model_class", MODELS + ENUMS)
def test_export_all(model_class: type, depth: str):
    """Make sure we find those models in the base."""
    package_root = import_module(model_class.__module__.split(".")[0] + depth)
    print("Expected in", package_root.__file__, ":")
    print("__all__ =", (UPDATED_PACKAGE_ALL if depth == "" else UPDATED_MODELS_ALL))
    assert model_class.__name__ in package_root.__all__
    assert getattr(package_root, model_class.__name__) is model_class
