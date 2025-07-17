def markdown_to_blocks(markdown):
    """
    Splits a markdown string into blocks separated by one or more blank lines.
    Strips leading/trailing whitespace from each block and removes empty blocks.
    """
    # Split strictly on double newlines (\n\n)
    blocks = markdown.split("\n\n")
    # Strip whitespace and remove empty blocks
    return [block.strip() for block in blocks if block.strip()]
