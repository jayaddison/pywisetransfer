import requests
from apiron import JsonEndpoint
from munch import munchify

from pytransferwise.base import Base
from pytransferwise import sca


class BorderlessAccountService(Base):
    list = JsonEndpoint(path="/v1/borderless-accounts", required_params=["profileId"])
    statement = JsonEndpoint(
        path="/v3/profiles/{profile_id}/borderless-accounts/{account_id}/statement.json",
        required_params=["currency", "intervalStart", "intervalEnd", "type"],
    )


class BorderlessAccount(object):
    service = BorderlessAccountService()

    def list(self, profile_id):
        return munchify(self.service.list(params={"profileId": profile_id}))

    def statement(self, profile_id, account_id, currency, interval_start, interval_end, statement_type='COMPACT'):
        try:  # apiron lib call response.raise_for_status() ans has no option to switch it off
            r = self.service.statement(
                profile_id=profile_id,
                account_id=account_id,
                params={
                    "currency": currency,
                    "intervalStart": interval_start,
                    "intervalEnd": interval_end,
                    "type": statement_type
                },
                return_raw_response_object=True  # Set this to analyze response status code for 403 in case of SCA
            )
        except requests.exceptions.HTTPError as e:
            r = e.response

            # Adopted from https://github.com/jtrotsky/tw-sca-signatures/blob/main/get-statements-sca.py
            # 403 with 'x-2fa-approval' header means that TW server ask for SCA
            if r.status_code == 403 and r.headers.get('x-2fa-approval') is not None:
                one_time_token = r.headers.get('x-2fa-approval')
                self.service = sca.add_sca_headers(self.service, one_time_token)
                return munchify(
                    self.service.statement(
                        profile_id=profile_id,
                        account_id=account_id,
                        params={
                            "currency": currency,
                            "intervalStart": interval_start,
                            "intervalEnd": interval_end,
                            "type": statement_type
                        },
                        return_raw_response_object=False
                    )
                )
            else:
                return munchify(r.json())
        else:
            if r.status_code == 200 or r.status_code == 201:
                return munchify(r.json())
