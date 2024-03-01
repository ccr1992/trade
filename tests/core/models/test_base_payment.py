import unittest
from core.models.payment_base import PaymentBase
from core.models.pay_types import PayTypes

from pydantic import ValidationError
from unittest.mock import patch, MagicMock

class TestPaymentBase(unittest.TestCase):
    

    def test_pay_with_invalid_param(self):
        payment = PaymentBase(value=500)
        price = 100
        with self.assertRaises(NotImplementedError):
            payment.pay(price, "Invalid_type")


if __name__ == '__main__':
    unittest.main()