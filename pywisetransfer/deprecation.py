from __future__ import annotations

import warnings


def deprecated(message, *args, **kwargs):
    """Decorator to indicate that a method is deprecated, with an optional
    message to emit in the warning.

    Written following guidance from:
    https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-iii-decorators-with-arguments
    """

    # Special-case: a decorator with no arguments is called with a single argument
    if not args and not kwargs and callable(message):
        warnings.warn(message, DeprecationWarning, stacklevel=2)
        return message

    # General-case: handle decorators with arguments; @deprecated(message='foo')
    def decorator(f):

        def deprecation_notice(*args, **kwargs):
            warnings.warn(message, DeprecationWarning, stacklevel=2)
            return f(*args, **kwargs)

        return deprecation_notice

    return decorator
