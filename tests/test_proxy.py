from unittest import TestCase
from unittest.mock import patch

from pythonlambdautils import Proxy


class ProxyTest(TestCase):
    def setUp(self) -> None:
        self.patcher = patch("pythonlambdautils.proxy.requests.get")
        self.mock_requests_get = self.patcher.start()

    def tearDown(self) -> None:
        self.patcher.stop()

    def test_get(self):
        proxy = Proxy("http://example.com")
        proxy.get()
        self.mock_requests_get.assert_called_once_with(
            url="http://example.com", params=None
        )

    def test_get_with_params(self):
        proxy = Proxy("http://example.com", params={"foo": "bar"})
        proxy.get()
        self.mock_requests_get.assert_called_once_with(
            url="http://example.com", params={"foo": "bar"}
        )
