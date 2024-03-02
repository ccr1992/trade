from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from api.main import app
from core.models.imputs.pipeline import Pipeline
from core.models.fiat_payment import FiatPayment
from core.models.outputs.user_resume import UserResume
import unittest
import httpx

client = TestClient(app)


class TestUserRouter(unittest.TestCase):
    payment = FiatPayment()
    fake_pipeline = Pipeline(payment=payment, trade_id=1234)
    fake_user_resume = UserResume(user_id=1, pending=4.4, paid=6.8)


    @patch(
        "api.routers.public_routers.execute_pipeline"
    )
    def test_create_payment_pipeline(self, mock_response: MagicMock) -> None:
        response: httpx.Response = client.post(
            "/public_methods/create_payment_pipeline/",
            json= self.fake_pipeline.model_dump()
        )
        self.assertEqual(response.status_code, 200)


    def test_create_payment_pipeline_validation_input_error(self) -> None:
        response: httpx.Response = client.post(
            "/public_methods/create_payment_pipeline/",
            json={
                "invalid_params": "1",
            },
        )
        self.assertEqual(response.status_code, 422)



    @patch(
        "api.routers.public_routers.get_user_resume"
    )
    def test_get_user_resume(self, mocked_method: MagicMock,
    ) -> None:
        mocked_method.return_value = self.fake_user_resume

        response: httpx.Response = client.get(
            "/public_methods/get_user_resume/1")
        self.assertEqual(response.status_code, 200)

