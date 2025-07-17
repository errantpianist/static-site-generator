from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        # Allow value to be None only for img tags
        if self.tag == "img":
            # Render as self-closing tag
            return f'<img{super().props_to_html()} />'
        if not self.value:
            raise ValueError("All leaf nodes except <img> must have a value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
        
