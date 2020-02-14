import unittest
from store import coupon_calculations


class MyTestCase(unittest.TestCase):
    def test_price_under_ten_1(self):
        self.assertEqual(8.49, coupon_calculations.calculate_price(8.00, 5.00, .10))

    # The following tests default to the 5.95 shipping cost since the item price will be zero when it matches or is
    # less than the cash-off coupon amount.
    def test_price_under_ten_2(self):
        self.assertEqual(5.95, coupon_calculations.calculate_price(5.00, 5.00, .15))

    def test_price_under_ten_3(self):
        self.assertEqual(5.95, coupon_calculations.calculate_price(1.00, 5.00, .20))

    def test_price_under_ten_4(self):
        self.assertEqual(5.95, coupon_calculations.calculate_price(9.99, 10.00, .10))

    def test_price_under_ten_5(self):
        self.assertEqual(5.95, coupon_calculations.calculate_price(0.01, 10.00, .15))

    def test_price_under_ten_6(self):
        self.assertEqual(5.95, coupon_calculations.calculate_price(5.00, 10.00, .20))


if __name__ == '__main__':
    unittest.main()
