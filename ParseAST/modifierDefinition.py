class ModifierDefinition:
    registry = []
    nodeType = "ModifierDefinition"

    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.documentation = node.get("documentation")
        self.id = node.get("id")
        self.name = node.get("name")
        self.parameters = node.get("parameters")
        self.src = node.get("src")
        self.visibility = node.get("visibility")
        
