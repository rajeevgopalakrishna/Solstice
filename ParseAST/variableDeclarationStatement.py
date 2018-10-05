class VariableDeclarationStatement:
    registry = []
    nodeType = "VariableDeclarationStatement"

    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.id = node.get("id")
        self.initialValue = node.get("initialValue")
        self.src = node.get("src")
        self.assignments = node.get("assignments")
        self.declarations = node.get("declarations")
        
        
