from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from api.main import app
from core.models.imputs.pipeline import Pipeline
from core.models.fiat_payment import FiatPayment
from core.models.user_resume import UserResume
import unittest
import httpx
from core.db.database_helper import DatabaseHelper
from core.models.imputs.pipeline import Pipeline
from core.models.fiat_payment import FiatPayment
from core.models.user import User
from core.models.pay_types import PayTypes
from core.models.trade import Trade
from api.routers.public_routers import execute_pipeline
from parameterized import parameterized


client = TestClient(app)


class TestUserRouter(unittest.TestCase):
    payment = FiatPayment()
    fake_pipeline = Pipeline(payment=payment, trade_id=1234)
    fake_user_resume = UserResume(user_id=1, to_pay=4.4, paid=6.8)


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


    def get_pipeline(self, value=100):
        return Pipeline(payment= FiatPayment(value=value), trade_id = 1)

    def fake_user_type_a(*args, **kwargs):
        return User(id=9999999, pay_type=PayTypes.type_A)

    def fake_user_type_b(*args, **kwargs):
        return User(id=9999999, pay_type=PayTypes.type_B)

    def fake_trade():
        return Trade()


    @parameterized.expand([
        (100, 0, 2.9701),
        (20, 0, 0.59402),
        (88.8, 0, 2.6374487999999996),
        (256987, 0, 7632.770887)
    ])
    @patch.object(DatabaseHelper, "get_user", side_effect=fake_user_type_a)
    @patch.object(DatabaseHelper, "get_trade", return_value=fake_trade())
    @patch.object(DatabaseHelper, "add")
    @patch.object(DatabaseHelper, "update")
    def test_execute_pipeline_typeA(self, value, expected_to_pay, expected_paid, mocked_get_user: MagicMock, mocked_get_trade: MagicMock, mocked_add: MagicMock, mocked_update: MagicMock):
        pipeline = self.get_pipeline(value)
        user_resume = execute_pipeline(pipeline)
        self.assertEqual(user_resume.to_pay, expected_to_pay)
        self.assertEqual(user_resume.paid, expected_paid)

    @parameterized.expand([
        (100, 1.9801000000000002, 0.99),
        (20, 0.39602000000000004, 0.198),
        (88.8, 1.7583288, 0.8791199999999999),
        (256987, 5088.599587, 2544.1713)
    ])
    @patch.object(DatabaseHelper, "get_user", side_effect=fake_user_type_b)
    @patch.object(DatabaseHelper, "get_trade", return_value=fake_trade())
    @patch.object(DatabaseHelper, "add")
    @patch.object(DatabaseHelper, "update")
    def test_execute_pipeline_typeB(self, value, expected_to_pay, expected_paid, mocked_get_user: MagicMock, mocked_get_trade: MagicMock, mocked_add: MagicMock, mocked_update: MagicMock):
        pipeline = self.get_pipeline(value)
        user_resume = execute_pipeline(pipeline)
        self.assertEqual(user_resume.to_pay, expected_to_pay)
        self.assertEqual(user_resume.paid, expected_paid)
