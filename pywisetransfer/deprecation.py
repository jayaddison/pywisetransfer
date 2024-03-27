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
            global f
            f = orig = args[0]
            exec(
                f"""
class deprecated(deprecated):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def {f.__name__}(*args, **kwargs):
        import warnings
        warnings.warn({self.message!r}, DeprecationWarning, stacklevel=2)
        return orig(*args, **kwargs)

f = deprecated.{f.__name__}
""",
                locals(),
                globals(),
            )
            return f

        warnings.warn(self.message, DeprecationWarning, stacklevel=2)
        return self.f(*args, **kwargs)

    def __repr__(self):
        return repr(self.f).replace("<function ", "<function deprecated.")
