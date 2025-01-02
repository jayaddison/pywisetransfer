from __future__ import annotations

from typing import Any

from apiron import Service

from pywisetransfer import Client


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
    def param_value_to_str(cls, value: Any) -> str:
        """Turn a paramater value into a string.

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
        if isinstance(value, (str, int, float)):
            return str(value)
        if isinstance(value, list):
            return ",".join(cls.param_value_to_str(v) for v in value)
        if hasattr(value, "id"):
            return cls.param_value_to_str(value.id)
        if hasattr(value, "as_parameter"):
            return cls.param_value_to_str(value.as_parameter())
        raise ValueError(f"Unsupported parameter type: {type(value)}")

    @classmethod
    def get_params_for_endpoint(self, **kw) -> dict[str, str]:
        """Return the actual keyword arguments for the endpoint call.

        >>> Base.get_kw_for_endpoint(profile_id=1)
        {profileId: '1'}
        """
        wise_call_args = {}
        for py_arg, value in kw.items():
            wise_arg = "".join(s[0].upper() + s[1:] for s in py_arg.split("_"))
            wise_arg = wise_arg[0].lower() + wise_arg[1:]
            if value is not None:
                wise_call_args[wise_arg] = self.param_value_to_str(value)
        return wise_call_args


__all__ = ["Base"]
