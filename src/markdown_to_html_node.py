from htmlnode import HTMLNode
from split_blocks import markdown_to_blocks
from block_type import block_to_block_type, BlockType
from textnodetohtmlnode import text_node_to_html_node
from text_to_textnodes import text_to_textnodes

# Helper: convert text to list of HTMLNodes (for inline parsing)
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            text = block.replace("\n", " ")
            node = HTMLNode("p", children=text_to_children(text))
        elif block_type == BlockType.HEADING:
            level = min(len(block) - len(block.lstrip('#')), 6)
            text = block[level+1:].replace("\n", " ")  # skip # and space, flatten lines
            node = HTMLNode(f"h{level}", children=text_to_children(text))
        elif block_type == BlockType.CODE:
            code = block.strip('`').strip()
            code_node = HTMLNode("code", value=code+"\n")
            node = HTMLNode("pre", children=[code_node])
        elif block_type == BlockType.QUOTE:
            quote = ' '.join([line[1:].lstrip() for line in block.split('\n')])
            node = HTMLNode("blockquote", children=text_to_children(quote))
        elif block_type == BlockType.UNORDERED_LIST:
            items = [line[2:].replace("\n", " ") for line in block.split('\n')]
            li_nodes = [HTMLNode("li", children=text_to_children(item)) for item in items]
            node = HTMLNode("ul", children=li_nodes)
        elif block_type == BlockType.ORDERED_LIST:
            items = [line[line.find('. ')+2:].replace("\n", " ") for line in block.split('\n')]
            li_nodes = [HTMLNode("li", children=text_to_children(item)) for item in items]
            node = HTMLNode("ol", children=li_nodes)
        else:
            text = block.replace("\n", " ")
            node = HTMLNode("p", children=text_to_children(text))
        children.append(node)
    return HTMLNode("div", children=children)
