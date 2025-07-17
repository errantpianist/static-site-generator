from textnode import TextNode, TextType
from extractor import extract_markdown_images

def split_nodes_image(old_nodes):
    """
    Splits TEXT nodes in old_nodes by markdown images, converting them to IMAGE TextNodes.
    Non-TEXT nodes are passed through unchanged.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        text = node.text
        images = extract_markdown_images(text)
        if not images:
            new_nodes.append(node)
            continue
        while images:
            alt, url = images.pop(0)
            img_md = f"![{alt}]({url})"
            split_parts = text.split(img_md, 1)
            before = split_parts[0]
            after = split_parts[1] if len(split_parts) > 1 else ""
            if before:
                new_nodes.append(TextNode(before, TextType.NORMAL))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            text = after
        if text:
            new_nodes.append(TextNode(text, TextType.NORMAL))
    return [n for n in new_nodes if n.text or n.text_type == TextType.IMAGE]
