import unittest

from main import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_normal(self):
        node = TextNode("Test", TextType.NORMAL)
        converted_node = text_node_to_html_node(node)
        self.assertEqual(converted_node.value, node.text)
        self.assertEqual(converted_node.tag, None)
        
    def test_bold(self):
        node = TextNode("Test", TextType.BOLD)
        converted_node = text_node_to_html_node(node)
        self.assertEqual(converted_node.value, node.text)
        self.assertEqual(converted_node.tag, "b")
        
    def test_italic(self):
        node = TextNode("Test", TextType.ITALIC)
        converted_node = text_node_to_html_node(node)
        self.assertEqual(converted_node.value, node.text)
        self.assertEqual(converted_node.tag, "i")
        
    def test_code(self):
        node = TextNode("Test", TextType.CODE)
        converted_node = text_node_to_html_node(node)
        self.assertEqual(converted_node.value, node.text)
        self.assertEqual(converted_node.tag, "code")
        
    def test_link(self):
        node = TextNode("Test", TextType.LINK)
        converted_node = text_node_to_html_node(node)
        self.assertEqual(converted_node.value, node.text)
        self.assertEqual(converted_node.tag, "a")
        self.assertEqual(converted_node.props["href"], None)
        
    def test_image(self):
        node = TextNode("Test", TextType.IMAGE)
        converted_node = text_node_to_html_node(node)
        self.assertEqual(converted_node.value, "")
        self.assertEqual(converted_node.tag, "img")
        self.assertEqual(converted_node.props["src"], None)
        self.assertEqual(converted_node.props["alt"], None)
        
