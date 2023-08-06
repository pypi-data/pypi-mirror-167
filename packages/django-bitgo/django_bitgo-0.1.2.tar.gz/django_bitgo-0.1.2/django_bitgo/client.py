from re import L
import requests
import os
from django.conf import settings

from django_bitgo.exceptions import BitGoException


class BitGoClient(object):
    def __init__(self, access_token) -> None:
        """
        Initializes the BitGo Client

        :param str access_token: Access Token to authenticate with
        """

        self.access_token = access_token or os.env.get("BITGO_ACCESS_TOKEN")

        if not self.access_token:
            raise BitGoException("Access token is required to create a BitGoClient")

    def request(self, method="GET", headers={}, path="", payload={}):
        headers["Authorization"] = f"Bearer {self.access_token}"

        return requests.request(
            method=method,
            url=f"{self.get_api_url()}{path}",
            headers=headers,
            data=payload,
        )

    def get_api_url(self):
        return settings.BITGO_API_URL
