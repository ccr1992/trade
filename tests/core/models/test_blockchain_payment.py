import unittest
from core.models.blockchain_payment import BlockchainPayment
from pydantic import ValidationError

class TestBlockchainPayment(unittest.TestCase):
    def test_payment_creation(self):
        payment = BlockchainPayment(id=1, value=100, full_paid=True)

        self.assertEqual(payment.id, 1)
        self.assertEqual(payment.value, 100)
        self.assertEqual(payment.full_paid, True)
        

    def test_default_values(self):
        payment = BlockchainPayment()

        self.assertEqual(payment.id, None)
        self.assertEqual(payment.value, None)
        self.assertEqual(payment.full_paid, False)

    def test_validation_payment_value(self):
        json_payment = {"id":1, "value":0}
        payment = BlockchainPayment()
        with self.assertRaises(ValidationError):
            payment.validate(json_payment)
    
    def test_validation_payment_negative_value(self):
        json_payment = {"id":1, "value":-100}
        payment = BlockchainPayment()
        with self.assertRaises(ValidationError):
            payment.validate(json_payment)

if __name__ == '__main__':
    unittest.main()