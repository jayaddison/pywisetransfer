"""Annotations to use."""

from typing import Annotated, TypeVar

from pydantic import PlainSerializer, BaseModel


def remove_none(model: BaseModel):
    """Remove None values from a model."""
    return model.model_dump(exclude_none=True)


T = TypeVar("T")

# class WithoutNone:
#     """Remove the fields with None from the value of this model."""

#     __slots__ = ()

#     def __new__(cls, *args, **kwargs):
#         raise TypeError("Type Annotated cannot be instantiated.")

#     def __class_getitem__(cls, params:T) -> Annotated[T, PlainSerializer]:
#         if isinstance(params, tuple):
#             raise TypeError(f"WithoutNone[...] should be used with one argument, not {params}")
#         return Annotated[params, PlainSerializer(remove_none)]

#     def __init_subclass__(cls, *args, **kwargs):
#         raise TypeError("Cannot subclass {}.WithoutNone".format(cls.__module__))


type WithoutNone[T] = Annotated[T, PlainSerializer(remove_none)]


__all__ = [
    "WithoutNone",
]
