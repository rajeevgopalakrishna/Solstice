class EventDefinition:
    registry = []
    nodeType = "EventDefinition"


    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.anonymous = node.get("anonymous'")
        self.documentation = node.get("documentation'")
        self.id = node.get("id'")
        self.name = node.get("name'")
        self.src = node.get("src'")
        
