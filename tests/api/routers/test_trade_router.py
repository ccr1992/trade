from fastapi.testclient import TestClient
from unittest.mock import call, patch, MagicMock

from api.main import app
from core.models.trade import Trade
import unittest
import httpx

client = TestClient(app)


class TestTradeRouter(unittest.TestCase):
    fake_trade = Trade(id=999)
    
    @patch(
        "api.routers.trade_routers.create_trade",
    )
    def test_create(self, mock_response: MagicMock,
    ) -> None:
        response: httpx.Response = client.post(
            "/trades/create/",
            json= self.fake_trade.model_dump()
        )
        self.assertEqual(response.status_code, 200)

    @patch(
        "api.routers.trade_routers.get_trade"
    )
    def test_get(self,mock_response: MagicMock,
    ) -> None:
        mock_response.return_value = self.fake_trade

        response: httpx.Response = client.get(
            "/trades/get/1")
        self.assertEqual(response.status_code, 200)

