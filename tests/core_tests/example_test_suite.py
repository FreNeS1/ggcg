import unittest

import ggcg


class ExampleTestSuite(unittest.TestCase):
    """Test cases fpr ggcg core_tests."""

    def test_example_sum(self):
        self.assertEqual(ggcg.core.example_sum(1, 2), 3)
        self.assertEqual(ggcg.core.example_sum(62, 21), 83)
        self.assertEqual(ggcg.core.example_sum(10, 22), 32)


if __name__ == '__main__':
    unittest.main()
