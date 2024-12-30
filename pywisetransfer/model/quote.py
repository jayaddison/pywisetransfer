"""The Quote resource

See https://docs.wise.com/api-docs/api-reference/quote#object
"""

from pydantic import BaseModel
from .uuid import UUID

class Quote(BaseModel):
    """The Quote object.
    
    See https://docs.wise.com/api-docs/api-reference/quote#object
    """
    id: str = UUID
    sourceCurrency: 