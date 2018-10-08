class FunctionDefinition:
    registry = []
    nodeType = "FunctionDefinition"

    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.documentation = node.get("documentation")
        self.id = node.get("id")
        self.implemented = node.get("implemented")
        self.isConstructor = node.get("isConstructor")
        self.isDeclaredConst = node.get("isDeclaredConst")
        self.modifiers = node.get("modifiers")
        self.name = node.get("name")
        self.parameters = node.get("parameters")
        self.payable = node.get("payable")
        self.returnParameters = node.get("returnParameters")
        self.scope = node.get("scope")
        self.src = node.get("src")
        self.stateMutability = node.get("stateMutability")
        self.superFunction = node.get("superFunction")
        self.visibility = node.get("visibility")
        
        
