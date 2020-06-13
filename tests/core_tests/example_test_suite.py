"""Contains an example test suite"""

import unittest

import ggcg.core


class ExampleTestSuite(unittest.TestCase):
    """Example test cases for the example class of ggcg."""

    def test_example_sum_(self):
        """
        Given: -
        When: Calling the `example_sum` function with 2 integers
        Then: Should return the added value of the integers.
        """
        self.assertEqual(ggcg.core.example_sum(1, 2), 3)
        self.assertEqual(ggcg.core.example_sum(62, 21), 83)
        self.assertEqual(ggcg.core.example_sum(10, 22), 32)


if __name__ == '__main__':
    unittest.main()
