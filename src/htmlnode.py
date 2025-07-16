class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        res = ""
        if self.props:
            for k, v in self.props.items():
                res += f' {k}="{v}"'
        return res

    def __repr__(self):
        print(f"HTMLNode (tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props})")
