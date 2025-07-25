import unittest
from block_type import block_to_block_type, BlockType

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### H6"), BlockType.HEADING)
        self.assertNotEqual(block_to_block_type("####### Not heading"), BlockType.HEADING)

    def test_code(self):
        self.assertEqual(block_to_block_type("```\ncode\n```"), BlockType.CODE)
        self.assertNotEqual(block_to_block_type("``\nnot code\n``"), BlockType.CODE)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> quote\n> more"), BlockType.QUOTE)
        self.assertNotEqual(block_to_block_type("> quote\nnot quote"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- item1\n- item2"), BlockType.UNORDERED_LIST)
        self.assertNotEqual(block_to_block_type("- item1\nitem2"), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. first\n2. second\n3. third"), BlockType.ORDERED_LIST)
        self.assertNotEqual(block_to_block_type("1. first\n3. third"), BlockType.ORDERED_LIST)
        self.assertNotEqual(block_to_block_type("1. first\n2. second\n2. third"), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("Just a paragraph."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("Not a list\nNot a heading"), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
