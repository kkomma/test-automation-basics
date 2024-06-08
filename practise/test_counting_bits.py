import unittest
from test_bank_operations import count_bits, is_power_of_two, is_divisible_by_two

class TestBankOperations(unittest.TestCase):
    
    def test_count_bits(self):
        self.assertEqual(count_bits(0), 0)
        self.assertEqual(count_bits(1), 1)
        self.assertEqual(count_bits(2), 1)
        self.assertEqual(count_bits(3), 2)
        self.assertEqual(count_bits(4), 1)
        self.assertEqual(count_bits(5), 2)
        self.assertEqual(count_bits(6), 2)
        self.assertEqual(count_bits(7), 3)
        self.assertEqual(count_bits(8), 1)
        self.assertEqual(count_bits(9), 2)
    
    def test_is_power_of_two(self):
        self.assertTrue(is_power_of_two(1))
        self.assertTrue(is_power_of_two(2))
        self.assertFalse(is_power_of_two(3))
        self.assertTrue(is_power_of_two(4))
        self.assertFalse(is_power_of_two(5))
        self.assertFalse(is_power_of_two(6))
        self.assertFalse(is_power_of_two(7))
        self.assertTrue(is_power_of_two(8))
        self.assertFalse(is_power_of_two(9))
    
    def test_is_divisible_by_two(self):
        self.assertTrue(is_divisible_by_two(0))
        self.assertTrue(is_divisible_by_two(2))
        self.assertFalse(is_divisible_by_two(3))
        self.assertTrue(is_divisible_by_two(4))
        self.assertFalse(is_divisible_by_two(5))
        self.assertFalse(is_divisible_by_two(6))
        self.assertFalse(is_divisible_by_two(7))
        self.assertTrue(is_divisible_by_two(8))
        self.assertFalse(is_divisible_by_two(9))

if __name__ == '__main__':
    unittest.main()