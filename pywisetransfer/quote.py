"""In order to create transfers, you have to create a quote.

The quote resource defines the basic information required for a Wise transfer - the currencies to send between, the amount to send and the profile who is sending the money. The profile must be included when creating a quote.

Quote is one of the required resources to create a transfer, along with the recipient who is to receive the funds.

The quote response contains other information such as the exchange rate, the estimated delivery time and the methods the user can pay for the transfer. Not all of this information may apply to your use case.

Upon creating a quote the current mid-market exchange rate is locked and will be used for the transfer that is created from the quote. The rate will be locked for 30 minutes to give a user time to complete the transfer creation flow.
"""
