import unittest
from src.extractor import extract_markdown_images, extract_markdown_links, extract_title

class TestExtractor(unittest.TestCase):
    def test_extract_markdown_images_single(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_multiple(self):
        text = "![one](url1) and ![two](url2)"
        expected = [("one", "url1"), ("two", "url2")]
        self.assertListEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_none(self):
        text = "No images here!"
        self.assertListEqual(extract_markdown_images(text), [])

    def test_extract_markdown_images_edge_cases(self):
        text = "![alt text]() and ![](url)"
        expected = [("alt text", ""), ("", "url")]
        self.assertListEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links_single(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        expected = [("to boot dev", "https://www.boot.dev")]
        self.assertListEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_multiple(self):
        text = "[one](url1) and [two](url2)"
        expected = [("one", "url1"), ("two", "url2")]
        self.assertListEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_none(self):
        text = "No links here!"
        self.assertListEqual(extract_markdown_links(text), [])

    def test_extract_markdown_links_edge_cases(self):
        text = "[text]() and [](url)"
        expected = [("text", ""), ("", "url")]
        self.assertListEqual(extract_markdown_links(text), expected)

    def test_links_do_not_match_images(self):
        text = "![alt](imgurl) and [text](url)"
        expected = [("text", "url")]
        self.assertListEqual(extract_markdown_links(text), expected)

    def test_images_do_not_match_links(self):
        text = "![alt](imgurl) and [text](url)"
        expected = [("alt", "imgurl")]
        self.assertListEqual(extract_markdown_images(text), expected)

    # Tests for extract_title
    def test_extract_title_simple(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")

    def test_extract_title_leading_trailing_whitespace(self):
        md = "   #   Hello World   "
        self.assertEqual(extract_title(md), "Hello World")

    def test_extract_title_multiline(self):
        md = "Some intro\n# My Title\nMore text"
        self.assertEqual(extract_title(md), "My Title")

    def test_extract_title_no_h1(self):
        md = "## Subtitle\nNo h1 here"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_extract_title_first_h1(self):
        md = "# First\n# Second"
        self.assertEqual(extract_title(md), "First")
