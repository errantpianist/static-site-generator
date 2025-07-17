import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitterDelimiter(unittest.TestCase):
    def test_bold(self):
        nodes = [TextNode("This is **bold** text", TextType.NORMAL)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertTrue(any(n.text_type == TextType.BOLD for n in result))
