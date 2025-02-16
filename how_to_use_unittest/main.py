import unittest


class Calculator:
    """基本的な算術演算を行うクラス

    このクラスは単純な計算機能を提供し、テストの例示に使用します。
    """

    def add(self, x, y):
        """2つの数値を加算します"""
        return x + y

    def divide(self, x, y):
        """除算を行います。ゼロ除算時はValueErrorを発生させます"""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(3, 5)
        self.assertEqual(result, 8, "3 + 5 should equal 8")

    def test_division_by_zero(self):
        # 0 除算がエラーになるかを検証
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)

        # 例外メッセージの検証
        self.assertTrue("Cannot divide by zero" in str(context.exception))

    def test_multiple_additions(self):
        test_cases = [(3, 5, 8), (-1, 1, 0), (100, 200, 300)]

        for x, y, expected in test_cases:
            with self.subTest(x=x, y=y, expected=expected):
                result = self.calc.add(x, y)
                self.assertEqual(result, expected)
