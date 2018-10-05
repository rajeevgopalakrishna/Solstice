class ExpressionStatement:
    registry = []
    nodeType = "ExpressionStatement"
            
    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.expression = node.get("expression")
        self.id = node.get("id")
        self.src = node.get("src")
