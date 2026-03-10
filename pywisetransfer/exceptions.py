from dataclasses import dataclass


class WiseException(Exception):
    pass


@dataclass
class WiseAccessDeniedException(WiseException):
    code: str | None = None
    message: str | None = None

    def __post_init__(self):
        super().__init__(self.message)


class InvalidWebhookHeader(WiseException):
    pass


class InvalidWebhookRequest(WiseException):
    pass


class InvalidWebhookSignature(WiseException):
    pass
