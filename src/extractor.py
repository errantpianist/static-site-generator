import re

def extract_markdown_images(text):
    """
    Extracts markdown images from text.
    Returns a list of (alt, url) tuples.
    """
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    """
    Extracts markdown links from text (not images).
    Returns a list of (text, url) tuples.
    """
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)
