import unittest
from hw import *


class TestHomeWork7(unittest.TestCase):

    """
    Test exercise-1
    """

    def test_is_prime(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(-3), False)
        self.assertEqual(is_prime(29), True)
        self.assertEqual(is_prime(7919), True)

    """
    Test exercise-2
    """

    def test_nth_fibonacci(self):
        self.assertEqual(nth_fibonacci(1), 0)
        self.assertEqual(nth_fibonacci(2), 1)
        self.assertEqual(nth_fibonacci(3), 1)
        self.assertEqual(nth_fibonacci(4), 2)
        self.assertEqual(nth_fibonacci(5), 3)
        self.assertEqual(nth_fibonacci(6), 5)
        self.assertEqual(nth_fibonacci(20), 4181)

    """
    Test exercise-3
    """

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    """
    Test exercise-4
    """

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("world"), 1)
        self.assertEqual(count_vowels("apple"), 2)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("a" * 1000), 1000)

    """
    Test exercise-5
    """

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(12345), 15)
        self.assertEqual(sum_of_digits(98765), 35)
        self.assertEqual(sum_of_digits(0), 0)
        self.assertEqual(sum_of_digits(-12345), 15)
        self.assertEqual(sum_of_digits(10000), 1)
        self.assertEqual(sum_of_digits(10 ** 1000 - 1), 9000)

    """
    Test exercise-6
    """

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("ab"), "ba")
        self.assertEqual(reverse_string("a" * 1000), "a" * 1000)

    """
    Test exercise-7
    """

    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares(1), 1)
        self.assertEqual(sum_of_squares(2), 5)
        self.assertEqual(sum_of_squares(3), 14)
        self.assertEqual(sum_of_squares(4), 30)
        self.assertEqual(sum_of_squares(5), 55)
        self.assertEqual(sum_of_squares(100), 338350)

    """
    Test exercise-8
    """

    # def test_collatz_sequence_length(self):
    #     self.assertEqual(collatz_sequence_length(6), 9)
    #     self.assertEqual(collatz_sequence_length(27), 112)
    #     self.assertEqual(collatz_sequence_length(1), 1)
    #     self.assertEqual(collatz_sequence_length(2), 2)
    #     self.assertEqual(collatz_sequence_length(10000), 30)

    """
    Test exercise-9
    """

    def test_is_leap_year(self):
        self.assertEqual(is_leap_year(2000), True)
        self.assertEqual(is_leap_year(1900), False)
        self.assertEqual(is_leap_year(2020), True)
        self.assertEqual(is_leap_year(2021), False)
        self.assertEqual(is_leap_year(10000), True)


    """
    Test exercise-10
    """

    def test_count_words(self):
        self.assertEqual(count_words("Hello world"), 2)
        self.assertEqual(count_words("This is a test"), 4)
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_words("a"), 1)
        self.assertEqual(count_words("word " * 1000), 1000)

    """
    Test exercise-11
    """

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("racecar"), True)
        self.assertEqual(is_palindrome("hello"), False)
        self.assertEqual(is_palindrome(""), True)
        self.assertEqual(is_palindrome("a"), True)
        self.assertEqual(is_palindrome("aa"), True)
        self.assertEqual(is_palindrome("ab"), False)

    """
    Test exercise-12
    """

    def test_sum_of_multiples(self):
        self.assertEqual(sum_of_multiples(10, 3, 5), 33)
        self.assertEqual(sum_of_multiples(20, 7, 11), 32)
        self.assertEqual(sum_of_multiples(1, 1, 1), 1)
        self.assertEqual(sum_of_multiples(0, 1, 1), 0)
        self.assertEqual(sum_of_multiples(1000, 3, 5), 234168)

    """
    Test exercise-13
    """

    def test_gcd(self):
        self.assertEqual(gcd(56, 98), 14)
        self.assertEqual(gcd(27, 15), 3)
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(1000000, 500000), 500000)

    """
    Test exercise-14
    """

    def test_lcm(self):
        self.assertEqual(lcm(5, 7), 35)
        self.assertEqual(lcm(6, 8), 24)
        self.assertEqual(lcm(1, 1), 1)
        self.assertEqual(lcm(0, 0), 0)
        self.assertEqual(lcm(1000, 500), 1000)

    """
    Test exercise-15
    """

    def test_count_characters(self):
        self.assertEqual(count_characters("hello world", "l"), 3)
        self.assertEqual(count_characters("apple", "p"), 2)
        self.assertEqual(count_characters("", "a"), 0)
        self.assertEqual(count_characters("a", "a"), 1)
        self.assertEqual(count_characters("ab", "a"), 1)
        self.assertEqual(count_characters("a" * 1000, "a"), 1000)

    """
    Test exercise-16
    """

    def test_digit_count(self):
        self.assertEqual(digit_count(123), 3)
        self.assertEqual(digit_count(4567), 4)
        self.assertEqual(digit_count(0), 1)
        self.assertEqual(digit_count(1), 1)
        self.assertEqual(digit_count(1000000), 7)

    """
    Test exercise-17
    """

    def test_is_power_of_two(self):
        self.assertEqual(is_power_of_two(8), True)
        self.assertEqual(is_power_of_two(10), False)
        self.assertEqual(is_power_of_two(1), True)
        self.assertEqual(is_power_of_two(2), True)
        self.assertEqual(is_power_of_two(1024), True)

    """
    Test exercise-18
    """

    def test_sum_of_cubes(self):
        self.assertEqual(sum_of_cubes(3), 36)
        self.assertEqual(sum_of_cubes(4), 100)
        self.assertEqual(sum_of_cubes(1), 1)
        self.assertEqual(sum_of_cubes(2), 9)
        self.assertEqual(sum_of_cubes(20), 44100)

    """
    Test exercise-19
    """

    def test_is_perfect_square(self):
        self.assertEqual(is_perfect_square(9), True)
        self.assertEqual(is_perfect_square(10), False)
        self.assertEqual(is_perfect_square(1), True)
        self.assertEqual(is_perfect_square(4), True)
        self.assertEqual(is_perfect_square(1000000), True)

    """
    Test exercise-20
    """

    def test_is_armstrong_number(self):
        self.assertEqual(is_armstrong_number(153), True)
        self.assertEqual(is_armstrong_number(370), True)
        self.assertEqual(is_armstrong_number(371), True)
        self.assertEqual(is_armstrong_number(9474), True)
        self.assertEqual(is_armstrong_number(9475), False)


if __name__ == '__main__':
    unittest.main()
