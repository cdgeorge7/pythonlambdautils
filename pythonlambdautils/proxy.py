from typing import Optional

import requests


class Proxy:
    def __init__(self, url: str, params: Optional[dict] = None):
        self.url = url
        self.params = params

    def get(self) -> requests.Response:
        return requests.get(url=self.url, params=self.params)
