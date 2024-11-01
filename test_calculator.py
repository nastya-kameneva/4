# test_chet.py

import unittest
from chet import divide, is_even

class TestChet(unittest.TestCase):

  def test_divide_by_zero(self):
    with self.assertRaises(ValueError):
      divide(10, 0)

  def test_is_even(self):
    self.assertTrue(is_even(4))
    self.assertFalse(is_even(3))

if __name__ == '__main__':
  unittest.main()
