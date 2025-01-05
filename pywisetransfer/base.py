from __future__ import annotations

from typing import Any
from uuid import UUID

from apiron import Service
from apiron.client import call as apiron_call


from pywisetransfer import Client
from pywisetransfer.model.base import BaseModel


class Base(Service):

    client: Client | None = None

    def __init__(self, *args: Any, **kwargs: Any):
        # TODO: It would be nice to make 'client' a required argument here
        # Currently apiron performs a zero-argument constructor call to the
        # service base class to retrieve the 'required_headers' property,
        # so we cater for empty arguments here
        # https://github.com/ithaka/apiron/blob/v5.1.0/src/apiron/service/base.py#L7
        if "client" in kwargs and Base.client != kwargs["client"]:
            Base.client = kwargs["client"]
        if Base.client and Base.client.environment == "live":
            Base.domain = "https://api.transferwise.com"
        else:
            Base.domain = "https://api.sandbox.transferwise.tech"

    @property
    def required_headers(self) -> dict[str, str]:  # type: ignore[override]
        if self.client:
            return {"Authorization": f"Bearer {self.client.api_key}"}
        return {}

    @classmethod
    def param_value_to_str(cls, value: Any, key: str = "") -> str:
        """Turn a paramater value into a string.

        >>> from pywisetransfer.base import Base
        >>> Base.param_value_to_str("test")
        'test'
        >>> Base.param_value_to_str(1)
        '1'
        >>> Base.param_value_to_str(True)
        'true'
        >>> Base.param_value_to_str(False)
        'false'

        """
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, (str, int, float, UUID)):
            return str(value)
        if isinstance(value, list):
            return ",".join(cls.param_value_to_str(v) for v in value)
        if hasattr(value, "as_parameter"):
            return cls.param_value_to_str(value.as_parameter())
        if hasattr(value, "id"):
            return cls.param_value_to_str(value.id)
        raise ValueError(
            f"Unsupported parameter type: {type(value)} value: {value}"
            + (f" key: {key}" if key else "")
        )

    @classmethod
    def get_params_for_endpoint(cls, **kw) -> dict[str, str]:
        """Return the actual keyword arguments for the endpoint call.

        >>> from pywisetransfer.base import Base
        >>> Base.get_params_for_endpoint(profile_id=1)
        {'profileId': '1'}

        """
        wise_call_args = {}
        for py_arg, value in kw.items():
            wise_arg = "".join(s[0].upper() + s[1:] for s in py_arg.split("_"))
            wise_arg = wise_arg[0].lower() + wise_arg[1:]
            if value is not None:
                wise_call_args[wise_arg] = cls.param_value_to_str(value, wise_arg)
        return wise_call_args

    @classmethod
    def adjust_endpoint_call(cls, kwargs: dict[str, Any]) -> dict[str, Any]:
        """Replace the call arguments so that it is more convenient to use."""
        leave_untouched = apiron_call.__code__.co_varnames
        for key, value in kwargs.items():
            if key not in leave_untouched:
                kwargs[key] = cls.param_value_to_str(value, key)
        if "params" in kwargs:
            kwargs["params"] = cls.get_params_for_endpoint(**kwargs["params"])
        if "json" in kwargs and isinstance(kwargs["json"], BaseModel):
            # print("base model", type(kwargs["json"]))
            kwargs["json"] = kwargs["json"].model_dump()
        return kwargs


__all__ = ["Base"]
