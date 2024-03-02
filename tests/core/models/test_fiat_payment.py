import unittest
from core.models.fiat_payment import FiatPayment
from core.models.pay_types import PayTypes
from core.models.user_resume import UserResume

from unittest.mock import patch, MagicMock

class TestFiatPayment(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_payment = FiatPayment()
        self.resume = UserResume(to_pay=0, paid=0, user_id=1)

    def test_payment_creation(self):
        payment = FiatPayment(id=1, value=100, full_paid=True, user_id=1, currency_code="USD")

        self.assertEqual(payment.id, 1)
        self.assertEqual(payment.value, 100)
        self.assertEqual(payment.full_paid, True)
        self.assertEqual(payment.user_id, 1)

    def test_default_values(self):
        self.assertEqual(self.empty_payment.id, None)
        self.assertEqual(self.empty_payment.value, None)
        self.assertEqual(self.empty_payment.full_paid, False)
        self.assertEqual(self.empty_payment.user_id, None)


    @patch.object(FiatPayment, 'convert')
    @patch.object(FiatPayment, '_pay_type_a')
    def test_pay_should_convert_before_pay(self, 
                                           mocked_method_convert: MagicMock,
                                           mocked_method_pay: MagicMock,
                                           ):
        empty_payment = FiatPayment(value=1)

        empty_payment.pay(PayTypes.type_A, self.resume)
        mocked_method_convert.assert_called_once()


if __name__ == '__main__':
    unittest.main()