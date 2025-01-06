"""Base class for models based on pydantic.

Attributes:
    DOCUMENTED_BUT_ABSENT: Alias of Optional to mark the absence of values from the documentation.
"""

from typing import ClassVar, Optional, Self
from pydantic import BaseModel


class BaseModel(BaseModel):
    """This is a base model.

    Attributes:
        EXAMPLE_JSON: A JSON that contains an example of this model.
    """

    EXAMPLE_JSON: ClassVar[str] = "{}"

    @classmethod
    def model_example(cls) -> Self:
        """Return an example of this model.

        If no example is set, this might well raise a ValidationError.
        """
        return cls.model_validate_json(cls.EXAMPLE_JSON)


DOCUMENTED_BUT_ABSENT = Optional
DEPRECATED = Optional

__all__ = ["BaseModel", "DOCUMENTED_BUT_ABSENT", "DEPRECATED"]
