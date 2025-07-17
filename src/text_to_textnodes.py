from textnode import TextNode, TextType
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from split_nodes_delimiter import split_nodes_delimiter

def text_to_textnodes(text):
    """
    Converts markdown-flavored text into a list of TextNode objects.
    Applies all splitters in the correct order.
    """
    nodes = [TextNode(text, TextType.NORMAL)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    return [n for n in nodes if n.text or n.text_type in (TextType.IMAGE, TextType.LINK)]
