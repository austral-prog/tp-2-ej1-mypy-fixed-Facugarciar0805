import unittest.mock
from src.maximums import max_of_two, max_of_three


class TP21MaximumsCases(unittest.TestCase):

    def test_max_of_two_positive(self)->None:
        result1 = max_of_two(5, 4)
        self.assertEqual(5, result1)

    def test_max_of_two_negative(self)->None:
        result2 = max_of_two(-2, -3)
        self.assertEqual(-2, result2)

    def test_max_of_two_equals(self)->None:
        result3 = max_of_two(0, 0)
        self.assertEqual(0, result3)

    def test_max_of_three_positive(self)->None:
        result4 = max_of_three(5, 4, 7)
        self.assertEqual(7, result4)

    def test_max_of_three_negative(self)->None:
        result5 = max_of_three(-2, -3, -1)
        self.assertEqual(-1, result5)

    def test_max_of_three_equals(self)->None:
        result6 = max_of_three(0, 0, 0)
        self.assertEqual(0, result6)


if __name__ == '__main__':
    unittest.main()
