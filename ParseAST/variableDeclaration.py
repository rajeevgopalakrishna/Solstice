class VariableDeclaration:
    registry = []
    nodeType = "VariableDeclaration"

    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.constant = node["constant"]
        self.id = node.get("id")
        self.name = node.get("name")
        self.scope = node.get("scope")
        self.src = node.get("src")
        self.stateVariable = node.get("stateVariable")
        self.storageLocation = node.get("storageLocation")
        self.typeDescriptions = node.get("typeDescriptions")
        self.typeName = node.get("typeName")
        self.value = node.get("value")
        self.visibility =  node.get("visibility")
        
        
