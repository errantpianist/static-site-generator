import unittest
from textnode import TextNode, TextType
from splitter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_no_delimiter(self):
        node = TextNode("This is plain text", TextType.NORMAL)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [node])

    def test_single_code(self):
        node = TextNode("This is `code` text", TextType.NORMAL)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_multiple_code(self):
        node = TextNode("A `b` c `d` e", TextType.NORMAL)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("A ", TextType.NORMAL),
            TextNode("b", TextType.CODE),
            TextNode(" c ", TextType.NORMAL),
            TextNode("d", TextType.CODE),
            TextNode(" e", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_bold(self):
        node = TextNode("This is **bold** text", TextType.NORMAL)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_italic(self):
        node = TextNode("This is _italic_ text", TextType.NORMAL)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_unmatched_delimiter(self):
        node = TextNode("This is `unmatched text", TextType.NORMAL)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_non_normal_node(self):
        node = TextNode("already bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, [node])

    def test_empty_string(self):
        node = TextNode("", TextType.NORMAL)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [node])

    def test_multiple_nodes(self):
        nodes = [
            TextNode("A `b`", TextType.NORMAL),
            TextNode("c", TextType.CODE),
            TextNode(" d `e` f", TextType.NORMAL),
        ]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = [
            TextNode("A ", TextType.NORMAL),
            TextNode("b", TextType.CODE),
            TextNode("", TextType.NORMAL),
            TextNode("c", TextType.CODE),
            TextNode(" d ", TextType.NORMAL),
            TextNode("e", TextType.CODE),
            TextNode(" f", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
