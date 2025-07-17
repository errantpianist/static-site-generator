import unittest
from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType

class TestSplitterLink(unittest.TestCase):
    def test_link(self):
        nodes = [TextNode("This is a [link](url) text", TextType.NORMAL)]
        result = split_nodes_link(nodes)
        self.assertTrue(any(n.text_type == TextType.LINK for n in result))
