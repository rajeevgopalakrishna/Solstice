from ParseAST.variableDeclaration import VariableDeclaration

class AnalyseVariable:
    def getAllVariables():
        return VariableDeclaration.registry

    def getAllStateVariables():
        stateVariables = []
        for variable in VariableDeclaration.registry:
            if (variable.stateVariable):
                stateVariables.append(variable)
        return stateVariables

    def getAllStorageVariables():
        storageVariables = []
        for variable in VariableDeclaration.registry:
            if (variable.storageLocation == "storage"):
                storageVariable.append(variable)
        return storageVariables

    def getAllMemoryVariables():
        memoryVariables = []
        for variable in VariableDeclaration.registry:
            if (variable.storageLocation == "memory"):
                memoryVariable.append(variable)
        return memoryVariables

    
        
                
        
    

    
    
    
