class FunctionCall:
    registry = []
    nodeType = "FunctionCall"

    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.argumentTypes = node.get("argumentTypes'")
        self.arguments = node.get("arguments'")
        self.expression = node.get("expression'")
        self.id = node.get("id'")
        self.isConstant = node.get("isConstant'")
        self.isLValue = node.get("isLValue'")
        self.isPure = node.get("isPure'")
        self.kind = node.get("kind'")
        self.lValueRequested = node.get("lValueRequested'")
        self.names = node.get("names'")
        self.src = node.get("src'")
        self.typeDescriptions = node.get("typeDescriptions'")
        self.name = node.get("expression").get("name")
