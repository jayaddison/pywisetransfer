"""An error response from Wise."""

from typing import ClassVar, Optional
from pydantic import BaseModel


class WiseAPIErrorResponse(BaseModel):
    """A model for errors coming from the API.

    Attributes:
        type: The type of the error
        title: The title of the error
        status: The status code of the error
        detail: A more detailed message of the error
        instance: The url path component of the error
        original_json: the original JSON response
    """

    EXAMPLE_JSON : ClassVar = """{
            "type":"about:blank",
            "title":"Unsupported Media Type",
            "status":415,
            "detail":"Content-Type'null' is not supported.",
            "instance":"/public/v3/quotes"
        }"""
    type: str
    title: str
    status: int
    detail: str
    instance: str
    original_json: Optional[dict] = None
    
__all__ = ["WiseAPIErrorResponse"]
