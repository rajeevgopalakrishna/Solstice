class IfStatement:
    registry = []
    nodeType = "IfStatement"

    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.condition = node.get("condition")
        self.trueBody = node.get("trueBody")
        self.falseBody = node.get("falseBody")
        self.id = node.get("id")
        self.src = node.get("src")
        
