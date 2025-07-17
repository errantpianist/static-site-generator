from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Splits NORMAL text nodes in old_nodes by the given delimiter, converting the delimited text to the given text_type.
    Non-NORMAL nodes are passed through unchanged.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) == 1:
            new_nodes.append(node)
            continue
        if len(parts) % 2 == 0:
            raise Exception(f"Invalid markdown syntax: unmatched delimiter '{delimiter}' in '{node.text}'")
        for i, part in enumerate(parts):
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.NORMAL))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes
