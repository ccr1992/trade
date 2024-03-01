import unittest
from core.models.fiat_payment import FiatPayment
from core.models.pay_types import PayTypes

from pydantic import ValidationError
from unittest.mock import patch, MagicMock

class TestFiatPayment(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_payment = FiatPayment()

    def test_payment_creation(self):
        payment = FiatPayment(id=1, value=100, full_paid=True, user_id=1)

        self.assertEqual(payment.id, 1)
        self.assertEqual(payment.value, 100)
        self.assertEqual(payment.full_paid, True)
        self.assertEqual(payment.user_id, 1)
        

    def test_default_values(self):
        self.assertEqual(self.empty_payment.id, None)
        self.assertEqual(self.empty_payment.value, None)
        self.assertEqual(self.empty_payment.full_paid, False)
        self.assertEqual(self.empty_payment.user_id, None)

    def test_validation_payment_value(self):
        json_payment = {"id":1, "value":0, "user_id":0}
        with self.assertRaises(ValidationError):
            self.empty_payment.validate(json_payment)
    
    def test_validation_payment_negative_value(self):
        json_payment = {"id":1, "value":-100, "user_id":0}
        with self.assertRaises(ValidationError):
            self.empty_payment.validate(json_payment)

    @patch.object(FiatPayment, 'convert')
    def test_pay_should_convert_before_pay(self, mocked_method: MagicMock):
        price_to_pay = 1000
        self.empty_payment.pay(price_to_pay, PayTypes.type_A)
        mocked_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()