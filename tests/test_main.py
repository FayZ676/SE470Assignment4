import unittest
from main import add, convert_markdown_to_html

class TestMain(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(2,3),5)

  def test_add_fail(self):
    # Intentionally failing test
    self.assertEqual(add(2, 3), 6)

  def test_mistune(self):
      sample_markdown = "# Hello world"
      self.assertEqual(convert_markdown_to_html(sample_markdown), 
                       '<h1>Hello world</h1>')

if __name__ == "__main__":
  unittest.main()
