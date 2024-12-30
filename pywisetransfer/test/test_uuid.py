"""Test the UUID functionality."""

import re
from pydantic import BaseModel, ValidationError
import pytest
from pywisetransfer.model.uuid import new_uuid, UUID, UUID_REGEX


def test_uuid_matches():
    """Check that the UUID matches the regex."""
    uuid = new_uuid()
    assert re.match(UUID_REGEX, uuid)


def test_uuid_differs():
    """Check that the UUIDs differ."""
    assert new_uuid() != new_uuid()


def test_uuid_is_str():
    """Check we have a string."""
    assert isinstance(new_uuid(), str)


def test_model_vaidation():
    """Check that the model validation works."""

    class M(BaseModel):
        uuid: str = UUID

    m = M(uuid=new_uuid())
    assert isinstance(m.uuid, str)
    with pytest.raises(ValidationError):
        M(uuid="not a uuid")
