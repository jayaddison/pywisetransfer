from __future__ import annotations

import warnings


class deprecated:
    """Decorator to indicate that a method is deprecated, with an optional
    message to emit in the warning.

    Written following guidance from:
    https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-iii-decorators-with-arguments
    """

    @staticmethod
    def _message(message=None, *args, **kwargs):
        return message

    def __init__(self, *args, **kwargs):
        self.f = None
        if args and callable(args[0]):
            self.f, args = args[0], args[1:]
        self.message = self._message(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if args and callable(args[0]) and not isinstance(args[0], deprecated):
            return deprecated(*args, message=self.message, **kwargs)

        warnings.warn(self.message, DeprecationWarning, stacklevel=2)
        return self.f(*args, **kwargs)

    def __repr__(self):
        return f"<deprecated {repr(self.f)}>"
