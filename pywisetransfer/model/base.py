"""Base class for models based on pydantic."""

from typing import ClassVar, Self
from pydantic import BaseModel


class BaseModel(BaseModel):
    """This is a base model.

    Attributes:
        EXAMPLE_JSON: A JSON that contains an example of this model.
    """

    EXAMPLE_JSON: ClassVar[str] = "{}"

    @classmethod
    def example(cls) -> Self:
        """Return an example of this model.

        If no example is set, this might well raise a ValidationError.
        """
        return cls.model_validate_json(cls.EXAMPLE_JSON)


__all__ = ["BaseModel"]
