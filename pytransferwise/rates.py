import requests
from apiron import JsonEndpoint
from munch import munchify

from pytransferwise.base import Base


class RatesService(Base):
    list = JsonEndpoint(path="/v1/rates")


class Rates(object):
    service = RatesService()

    def list(self, **kwargs):

        def lookup_param_names(p):
            return {
                    p == 'date_from': 'from',
                    p == 'date_to': 'to',
                    p not in ['date_from', 'date_to']: p
            }[True]

        if not kwargs:
            return munchify(self.service.list())
        else:
            params = {}
            for k in kwargs:
                k_l = lookup_param_names(k)
                params[k_l] = kwargs[k]
            return munchify(self.service.list(params=params))
