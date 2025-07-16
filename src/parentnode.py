from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag")
        if not self.children:
            raise ValueError("All parent nodes must have at least one child node")
        res = f"<{self.tag}{super().props_to_html()}>"
        for child in self.children:
            res += child.to_html()
        res += f"</{self.tag}>"
        return res

