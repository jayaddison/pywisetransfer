from __future__ import annotations

import warnings


class deprecated:
    """Decorator to indicate that a method is deprecated, with an optional
    message to emit in the warning.

    Written following guidance from:
    https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-iii-decorators-with-arguments
    """

    def __init__(self, *args, **kwargs):
        if len(args) == 1 and callable(args[0]):
            self.f = args[0]
            message = args[1] if len(args) > 1 else None
        else:
            self.f = None
            message = args[0] if len(args) == 1 else None
        self.message = kwargs.get("message", message)

    def __call__(self, *args, **kwargs):
        if self.f is None and len(args) == 1 and callable(args[0]):
            self.f = args[0]
            return self

        warnings.warn(self.message, DeprecationWarning, stacklevel=2)
        return self.f(*args, **kwargs)
