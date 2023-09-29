class WiseException(Exception):
    pass


class InvalidWebhookRequest(WiseException):
    pass


class InvalidWebhookSignature(WiseException):
    pass
