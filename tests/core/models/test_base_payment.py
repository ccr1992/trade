import unittest
from core.models.payment_base import PaymentBase
from core.models.pay_types import PayTypes

from pydantic import ValidationError
from unittest.mock import patch, MagicMock

class TestPaymentBase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.empty_payment = PaymentBase(value=10)

    def test_pay_with_invalid_param(self):
        payment = PaymentBase(value=500)
        with self.assertRaises(NotImplementedError):
            payment.pay("Invalid_type", "Fake user resume")

    def test_price_without_taxes(self):
        payment = PaymentBase(value=500)
        result = payment.price_without_taxes()
        self.assertEqual(result, 495)

    def test_price_without_taxes_with_decimals(self):
        payment = PaymentBase(value=55.5)
        result = payment.price_without_taxes()
        self.assertEqual(result, 54.945)


    def test_validation_payment_value(self):
        json_payment = {"id":1, "value":0, "user_id":0}
        with self.assertRaises(ValidationError):
            self.empty_payment.validate(json_payment)
    
    def test_validation_payment_negative_value(self):
        json_payment = {"id":1, "value":-100, "user_id":0}
        with self.assertRaises(ValidationError):
            self.empty_payment.validate(json_payment)

    def test_validation_payment_negative_tax(self):
        json_payment = {"id":1, "value":100, "tax": -1, "user_id":0}
        with self.assertRaises(ValidationError):
            self.empty_payment.validate(json_payment)

    def test_validation_payment_imposible_tax(self):
        json_payment = {"id":1, "value":100, "tax": 1.1, "user_id":0}
        with self.assertRaises(ValidationError):
            self.empty_payment.validate(json_payment)

if __name__ == '__main__':
    unittest.main()