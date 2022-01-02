class WiseException(Exception):
    pass


class InvalidWebhookHeader(WiseException):
    pass


class InvalidWebhookRequest(WiseException):
    pass


class InvalidWebhookSignature(WiseException):
    pass
