class Expression:
    registry = []

    def __init__(self, node, typeOfExpression):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.nodeType = node.get("nodeType")
        self.argumentTypes = node.get("argumentTypes")
        self.arguments = node.get("arguments")
        self.id = node.get("id")
        self.isConstant = node.get("isConstant")
        self.isLValue = node.get("isLValue")
        self.isPure = node.get("isPure")
        self.lValueRequested = node.get("lValueRequested")
        self.operator = node.get("operator")
        self.prefix = node.get("prefix")
        self.src = node.get("src")
        self.subExpression = node.get("subExpression")
        self.typeDescriptions = node.get("typeDescriptions")
        self.leftHandSide = node.get("leftHandSide")
        self.rightHandSide = node.get("rightHandSide")
        self.leftExpression = node.get("leftExpression")
        self.rightExpression = node.get("rightExpression")
        self.overloadedDeclarations = node.get("overloadedDeclarations")
        self.referencedDeclaration = node.get("referencedDeclaration")
        self.name = node.get("name")
        self.commonType = node.get("commonType")
        self.components = node.get("components")
        self.hexValue = node.get("hexValue")
        self.kind = node.get("kind")
        self.subdenomination = node.get("subdenomination")
        self.value = node.get("value")
        self.isInlineArray = node.get("isInlineArray")
        self.memberName = node.get("memberName")
        self.type = typeOfExpression
