"""Test the UUID functionality."""

from pydantic import BaseModel, ValidationError
import pytest
from wise_banking_api_client.model.uuid import new_uuid, UUID


class M(BaseModel):
    uuid: UUID


def test_uuid_differs():
    """Check that the UUIDs differ."""
    assert new_uuid() != new_uuid()


def test_uuid_is_str():
    """Check we have a string."""
    assert isinstance(new_uuid(), UUID)


def test_model_validation():
    """Check that the model validation works."""
    m = M(uuid=new_uuid())
    assert isinstance(m.uuid, UUID)
    m.model_validate(m)


def test_model_validation_str():
    """Check that the model validation works."""
    m = M(uuid=str(new_uuid()))
    m.model_validate(m)


def test_invalid_uuid():
    with pytest.raises(ValidationError):
        M(uuid="not a uuid")
