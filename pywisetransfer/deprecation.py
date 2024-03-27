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
        if len(args) == 1 and callable(args[0]):
            orig = args[0]
            exec(
                f"""
class deprecated(deprecated):
    @staticmethod
    def {orig.__name__}(*args, **kwargs):
        self._emit_warning()
        return orig(*args, **kwargs)

self.f = deprecated.{orig.__name__}
""",
                locals(),
                globals(),
            )
            args = args[1:]
        self.message = self._message(*args, **kwargs)

    def _emit_warning(self):
        warnings.warn(self.message, DeprecationWarning, stacklevel=3)

    def __call__(self, *args, **kwargs):
        if self.f:
            return self.f(*args, **kwargs)
        else:
            assert len(args) == 1 and callable(args[0])
            return deprecated(args[0], message=self.message).f

    def __repr__(self):
        if self.f:
            return repr(self.f)
        else:
            return f"<deprecation decorator ({self.message!r})>"
