class ContractDefinition:
    registry = []
    nodeType = "ContractDefinition"

    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.baseContracts = node.get("baseContracts")
        self.contractDependencies = node.get("contractDependencies")
        self.contractKind = node.get("contractKind")
        self.documentation = node.get("documentation")
        self.fullyImplemented = node.get("fullyImplemented")
        self.id = node.get("id")
        self.linearizedBaseContracts = node.get("linearizedBaseContracts")
        self.name = node.get("name")
        self.scope = node.get("scope")
        self.src = node.get("src")
        
