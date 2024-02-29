import unittest
from core.models.fiat_payment import FiatPayment
from pydantic import ValidationError

class TestFiatPayment(unittest.TestCase):
    def test_payment_creation(self):
        payment = FiatPayment(id=1, value=100, full_paid=True, user_id=1)

        self.assertEqual(payment.id, 1)
        self.assertEqual(payment.value, 100)
        self.assertEqual(payment.full_paid, True)
        self.assertEqual(payment.user_id, 1)
        

    def test_default_values(self):
        payment = FiatPayment()

        self.assertEqual(payment.id, None)
        self.assertEqual(payment.value, None)
        self.assertEqual(payment.full_paid, False)
        self.assertEqual(payment.user_id, None)

    def test_validation_payment_value(self):
        json_payment = {"id":1, "value":0, "user_id":0}
        payment = FiatPayment()
        with self.assertRaises(ValidationError):
            payment.validate(json_payment)
    
    def test_validation_payment_negative_value(self):
        json_payment = {"id":1, "value":-100, "user_id":0}
        payment = FiatPayment()
        with self.assertRaises(ValidationError):
            payment.validate(json_payment)

if __name__ == '__main__':
    unittest.main()