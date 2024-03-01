import unittest
from core.models.trade import Trade

class TestTrade(unittest.TestCase):
    def test_trade_creation(self):
        trade = Trade(id=1)

        self.assertEqual(trade.id, 1)


if __name__ == '__main__':
    unittest.main()