import unittest
from hw_bonus import *  


class TestFunctions(unittest.TestCase):
    """
    💎 Test exercise-1
    """

    def test_count_substrings(self):
        self.assertEqual(count_substrings("ababab", "ab"), 3)
        self.assertEqual(count_substrings("aaaaaa", "aa"), 3)
        self.assertEqual(count_substrings("hello world", "l"), 3)
        self.assertEqual(count_substrings("xyzxyzxyz", "xyz"), 3)
        self.assertEqual(count_substrings("a" * 1000, "aa"), 500)

    """
    💎 Test exercise-2
    """

    def test_find_smallest_divisor(self):
        self.assertEqual(find_smallest_divisor(21), 3)
        self.assertEqual(find_smallest_divisor(49), 7)
        self.assertEqual(find_smallest_divisor(169), 13)
        self.assertEqual(find_smallest_divisor(77), 7)
        self.assertEqual(find_smallest_divisor(123456789), 3)

    """
    💎 Test exercise-3
    """

    def test_check_divisible_by_any(self):
        self.assertEqual(check_divisible_by_any(24, "2 3 5"), True)
        self.assertEqual(check_divisible_by_any(23, "2 3 5"), False)
        self.assertEqual(check_divisible_by_any(20, "4 5 6"), True)
        self.assertEqual(check_divisible_by_any(19, "2 3 5"), False)
        self.assertEqual(check_divisible_by_any(123456789, "2 3 5 7 11"), True)

    """
    💎 Test exercise-4
    """

    def test_find_nth_root(self):
        self.assertAlmostEqual(find_nth_root(8, 3), 2.0, places=3)
        self.assertAlmostEqual(find_nth_root(81, 4), 3.0, places=3)
        self.assertAlmostEqual(find_nth_root(16, 4), 2.0, places=3)
        self.assertAlmostEqual(find_nth_root(100, 2), 10.0, places=3)
        self.assertAlmostEqual(find_nth_root(1000000, 6), 10.0, places=3)

    """
    💎 Test exercise-5
    """

    def test_collatz_sequence_length(self):
        self.assertEqual(collatz_sequence_length(6), 8)
        self.assertEqual(collatz_sequence_length(27), 111)
        self.assertEqual(collatz_sequence_length(12), 9)
        self.assertEqual(collatz_sequence_length(7), 16)
        self.assertEqual(collatz_sequence_length(999999), 258)


if __name__ == '__main__':
    unittest.main()
