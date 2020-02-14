import unittest
from store import coupon_calculations


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        with self.subTest():
            self.assertEqual(8.81, coupon_calculations.calculate_price(8.00, 5.00, .10))
        with self.subTest():
            self.assertEqual(5.95, coupon_calculations.calculate_price(5.00, 5.00, .15))
        with self.subTest():
            self.assertEqual(5.95, coupon_calculations.calculate_price(1.00, 5.00, .20))
        with self.subTest():
            self.assertEqual(5.95, coupon_calculations.calculate_price(9.99, 10.00, .10))
        with self.subTest():
            self.assertEqual(5.95, coupon_calculations.calculate_price(0.01, 10.00, .15))
        with self.subTest():
            self.assertEqual(5.95, coupon_calculations.calculate_price(5.00, 10.00, .20))

    def test_price_under_between_ten_thirty(self):
        with self.subTest():
            self.assertEqual(12.72, coupon_calculations.calculate_price(10.00, 5.00, .10))
        with self.subTest():
            self.assertEqual(21.46, coupon_calculations.calculate_price(20.00, 5.00, .15))
        with self.subTest():
            self.assertEqual(29.14, coupon_calculations.calculate_price(29.99, 5.00, .20))
        with self.subTest():
            self.assertEqual(7.95, coupon_calculations.calculate_price(10.00, 10.00, .10))
        with self.subTest():
            self.assertEqual(16.96, coupon_calculations.calculate_price(20.00, 10.00, .15))
        with self.subTest():
            self.assertEqual(24.90, coupon_calculations.calculate_price(29.99, 10.00, .20))

    def test_price_under_between_thirty_fifty(self):
        with self.subTest():
            self.assertEqual(35.80, coupon_calculations.calculate_price(30.00, 5.00, .10))
        with self.subTest():
            self.assertEqual(43.49, coupon_calculations.calculate_price(40.00, 5.00, .15))
        with self.subTest():
            self.assertEqual(50.10, coupon_calculations.calculate_price(49.99, 5.00, .20))
        with self.subTest():
            self.assertEqual(31.03, coupon_calculations.calculate_price(30.00, 10.00, .10))
        with self.subTest():
            self.assertEqual(38.98, coupon_calculations.calculate_price(40.00, 10.00, .15))
        with self.subTest():
            self.assertEqual(45.86, coupon_calculations.calculate_price(49.99, 10.00, .20))


if __name__ == '__main__':
    unittest.main()
