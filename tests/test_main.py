import unittest
from main import add

class TestAddition(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(2,3),5)

  def test_add_fail(self):
          # Intentionally failing test
          self.assertEqual(add(2, 3), 6)

if __name__ == "__main__":
  unittest.main()
