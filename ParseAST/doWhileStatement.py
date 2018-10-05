class DoWhileStatement:
    registry = []
    nodeType = "DoWhileStatement"

    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.condition = node.get("condition")
        self.body = node.get("body")
        self.id = node.get("id")
        self.src = node.get("src")
        
