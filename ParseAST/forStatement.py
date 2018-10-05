class ForStatement:
    registry = []
    nodeType = "ForStatement"

    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.body = node.get("body")
        self.condition = node.get("condition")
        self.initializationExpression = node.get("initializationExpression")
        self.loopExpression = node.get("loopExpression")
        self.id = node.get("id")
        self.src = node.get("src")
        
