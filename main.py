import mistune

def add(a,b):
  return a + b

def convert_markdown_to_html(markdown: str):
  return mistune.html(markdown)