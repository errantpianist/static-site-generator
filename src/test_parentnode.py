import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_1(self):
        node = ParentNode(
                 "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    def test_to_html_with_props(self):
        node = ParentNode(
                 "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
            {"test": "val"}
        )
        self.assertEqual(node.to_html(), '<p test="val"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    def test_to_html_div(self):
        node = ParentNode(
                 "div",
    [
        LeafNode("p", "text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
            {"prop": "test"}
        )
        self.assertEqual(node.to_html(), '<div prop="test"><p>text</p>Normal text<i>italic text</i>Normal text</div>')
