from fastapi.testclient import TestClient
from unittest.mock import call, patch, MagicMock

from api.main import app
from core.models.user import User, PayTypes
import unittest
import httpx

client = TestClient(app)


class TestUserRouter(unittest.TestCase):
    fake_user = User(id=1, pay_type=PayTypes.type_A, name="user_1")
    
    @patch(
        "api.routers.user_routers.create_user",
    )
    def test_create(self, mock_response: MagicMock,
    ) -> None:
        response: httpx.Response = client.post(
            "/users/create/",
            json= self.fake_user.model_dump()
        )
        self.assertEqual(response.status_code, 200)


    def test_create_validation_input_error(self) -> None:
        response: httpx.Response = client.post(
            "/users/create/",
            json={
                "invalid_params": "1",
            },
        )
        self.assertEqual(response.status_code, 422)

    @patch(
        "api.routers.user_routers.get_user"
    )
    def test_get(self,mock_response: MagicMock,
    ) -> None:
        mock_response.return_value = self.fake_user

        response: httpx.Response = client.get(
            "/users/get/1")
        self.assertEqual(response.status_code, 200)

