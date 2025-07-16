import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_1(self):
        node = HTMLNode("div", "test node", [], {"font-size": "18"})
        self.assertEqual(node.props_to_html(), ' font-size="18"')

    def test_props_to_html_2(self):
        node = HTMLNode("div", "test node", [], {"data-test": "42"})
        self.assertEqual(node.props_to_html(), ' data-test="42"')

    def test_props_to_html_multi(self):
        node = HTMLNode("div", "test node", [], {"font-size": "18", "background-color": "red"})
        self.assertEqual(node.props_to_html(), ' font-size="18" background-color="red"')
