from enum import Enum, auto
import re

class BlockType(Enum):
    PARAGRAPH = auto()
    HEADING = auto()
    CODE = auto()
    QUOTE = auto()
    UNORDERED_LIST = auto()
    ORDERED_LIST = auto()

def block_to_block_type(block):
    # Code block: starts and ends with 3 backticks
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    # Heading: 1-6 # followed by space
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    # Quote: every line starts with '>'
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    # Unordered list: every line starts with '- '
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    # Ordered list: every line starts with incrementing number + '. '
    if all(re.match(rf"{i+1}\. ", line) for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    # Default: paragraph
    return BlockType.PARAGRAPH
