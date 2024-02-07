import unittest
from main import add, convert_markdown_to_html

class TestAddition(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(2,3),5)

  def test_add_fail(self):
    # Intentionally failing test
    self.assertEqual(add(2, 3), 6)

  def test_mistune(self):
      sample_markdown = "**This is [a link with *nested* emphasis](https://example.com)**"
      self.assertEqual(convert_markdown_to_html(sample_markdown), 
                       '<p><strong>This is <a href="https://example.com"><em>a link with <strong>nested</strong> emphasis</em></a></strong></p>')

if __name__ == "__main__":
  unittest.main()
