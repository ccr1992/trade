import unittest
from core.models.user import User
from core.models.user_resume import UserResume
from pydantic import ValidationError

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(id=1, pay_type=1, name="Usuario_A", paid=100.0, to_pay=50.0)

        self.assertEqual(user.id, 1)
        self.assertEqual(user.pay_type, 1)
        self.assertEqual(user.name, "Usuario_A")
        self.assertEqual(user.paid, 100.0)
        self.assertEqual(user.to_pay, 50.0)

    def test_default_values(self):
        user = User()

        self.assertIsNone(user.id)
        self.assertIsNone(user.pay_type)
        self.assertIsNone(user.name)
        self.assertEqual(user.paid, 0.0)
        self.assertEqual(user.to_pay, 0.0)

    def test_validation_user_creation(self):
        json_user = {"id":1, "pay_type":"fake", "name":"Usuario_A", "paid":100.0, "to_pay":50.0}
        user = User()
        with self.assertRaises(ValidationError):
            user.validate(json_user)

    def test_get_user_resume(self):
        user = User(id=1, pay_type=1, name="Usuario_A", paid=100.0, to_pay=50.0)
        resume = user.get_user_resume()
        expected = UserResume(id=1, paid=100.0, to_pay=50.0)
        self.assertEqual(resume, expected)

if __name__ == '__main__':
    unittest.main()