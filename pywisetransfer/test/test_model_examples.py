"""Test all the examples."""

from pathlib import Path
from typing import Type

import pytest
import pywisetransfer.model
from importlib import import_module

from pywisetransfer.model.base import BaseModel

MODELS_WITH_EXAMPLES = []

MODEL_DIR = Path(pywisetransfer.model.__file__).parent
for file in MODEL_DIR.iterdir():
    if file.suffix.lower() == ".py":
        module = import_module(f"pywisetransfer.model.{file.stem}")
        for cls in module.__dict__.values():
            if isinstance(cls, type) and issubclass(cls, BaseModel):
                if cls.EXAMPLE_JSON != BaseModel.EXAMPLE_JSON:
                    MODELS_WITH_EXAMPLES.append(cls)


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
    print('    EXAMPLE_JSON : ClassVar[str] = """' + json + '"""')
    print()
    print("in", import_module(model_class.__module__).__file__, "->", model_class.__name__)
    assert e.EXAMPLE_JSON == json
