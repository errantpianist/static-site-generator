import unittest
from split_blocks import markdown_to_blocks

class TestSplitBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = (
            """This is **bolded** paragraph\n\nThis is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\n\n- This is a list\n- with items"""
        )
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_leading_trailing_whitespace(self):
        md = """\n\n   Block one   \n\n\nBlock two\n\n   \nBlock three   \n\n"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Block one", "Block two", "Block three"])

    def test_empty_blocks(self):
        md = """\n\n\n\n"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])