import unittest
from split_nodes_image import split_nodes_image
from textnode import TextNode, TextType

class TestSplitterImage(unittest.TestCase):
    def test_image(self):
        nodes = [TextNode("This is an image ![alt](url) text", TextType.NORMAL)]
        result = split_nodes_image(nodes)
        self.assertTrue(any(n.text_type == TextType.IMAGE for n in result))
