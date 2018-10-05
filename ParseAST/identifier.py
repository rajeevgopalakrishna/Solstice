class Identifier:
    registry = []

    def __init__(self, node, type):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.argumentTypes = node.get("argumentTypes")
        self.id = node.get("id")
        self.name = node.get("name")
        self.nodeType = node.get("nodeType")        
        self.overloadedDeclarations = node.get("overloadedDeclarations")
        self.referencedDeclaration = node.get("referencedDeclaration")
        self.typeIdentifier = node.get("typeDescriptions").get("typeIdentifier")
        self.type = type
