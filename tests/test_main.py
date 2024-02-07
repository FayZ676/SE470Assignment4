import unittest
from main import add, convert_markdown_to_html
import re

class TestMain(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(2,3),5)

  def test_add_intentional_fail(self):
    # Intentionally failing test
    self.assertEqual(add(2, 3), 6)

  def test_mistune_blockquote(self):
      sample_markdown = ">Hello world"
      self.assertEqual(convert_markdown_to_html(sample_markdown), 
                       '<blockquote>\n<p>Hello world</p>\n</blockquote>\n')
      
  def test_mistune_link_embedded(self):
    sample_link = "# [link](https://abc123.com)"
    self.assertEqual(convert_markdown_to_html(sample_link), '<h1><a href="https://abc123.com">link</a></h1>\n')

  def test_mistune_link_intentional_fail(self): 
    # Caught bug from issue https://github.com/lepture/mistune/issues/355
    sample_link = "[The Menu](https://en.wikipedia.org/wiki/The_Menu_(2022_film)) some text."
    self.assertEqual(convert_markdown_to_html(sample_link), '<p><a href="https://en.wikipedia.org/wiki/The_Menu_(2022_film)">The Menu</a> some text.</p>\n')

  def test_mistune_link_fixed(self): 
    def format_link(input_string):
        start_index = input_string.find('(')
        end_index = input_string.rfind(')')
        
        if start_index != -1 and end_index != -1 and end_index > start_index:
            extracted_content = input_string[start_index + 1:end_index]
            wrapped_content = f"<{extracted_content}>"
            formatted_string = input_string[:start_index + 1] + wrapped_content + input_string[end_index:]
            return formatted_string
        else:
            return None
    
    sample_link = "[The Menu](https://en.wikipedia.org/wiki/The_Menu_(2022_film)) some text."
    updated_link = format_link(sample_link)
    print(f"UPDATED LINK: {updated_link}")
    self.assertEqual(convert_markdown_to_html(updated_link), '<p><a href="https://en.wikipedia.org/wiki/The_Menu_(2022_film)">The Menu</a> some text.</p>\n')


if __name__ == "__main__":
  unittest.main()
