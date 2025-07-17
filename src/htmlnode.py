class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        # If node has children, render them recursively
        children_html = ''
        if self.children:
            children_html = ''.join(child.to_html() for child in self.children)
        # If node has a tag
        if self.tag:
            props_html = self.props_to_html()
            if self.value is not None:
                return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag}{props_html}>{children_html}</{self.tag}>'
        # If node has only value
        if self.value is not None:
            return self.value
        # If node has only children
        if self.children:
            return children_html
        return ''

    def props_to_html(self):
        res = ""
        if self.props:
            for k, v in self.props.items():
                res += f' {k}="{v}"'
        return res

    def __repr__(self):
        return f"HTMLNode (tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props})"
