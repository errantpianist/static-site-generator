from textnode import TextNode, TextType
from extractor import extract_markdown_links

def split_nodes_link(old_nodes):
    """
    Splits TEXT nodes in old_nodes by markdown links, converting them to LINK TextNodes.
    Non-TEXT nodes are passed through unchanged.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_links(text)
        if not links:
            new_nodes.append(node)
            continue
        while links:
            anchor, url = links.pop(0)
            link_md = f"[{anchor}]({url})"
            split_parts = text.split(link_md, 1)
            before = split_parts[0]
            after = split_parts[1] if len(split_parts) > 1 else ""
            if before:
                new_nodes.append(TextNode(before, TextType.NORMAL))
            new_nodes.append(TextNode(anchor, TextType.LINK, url))
            text = after
        if text:
            new_nodes.append(TextNode(text, TextType.NORMAL))
    return [n for n in new_nodes if n.text or n.text_type == TextType.LINK]
