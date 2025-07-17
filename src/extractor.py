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
    
def extract_title(markdown):
    """Extracts the first h1 header from the markdown string and returns its text. Raises an exception if not found."""
    for line in markdown.splitlines():
        if line.strip().startswith('# '):
            return line.strip()[2:].strip()
    raise Exception("No h1 header found in markdown.")
