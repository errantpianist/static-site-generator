import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_text_diff(self):
        node1 = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_type_diff(self):
        node1 = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_url_diff(self):
        node1 = TextNode("This is a test node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://google.co.uk")
        self.assertNotEqual(node1, node2)
