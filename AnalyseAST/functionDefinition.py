from ParseAST.functionDefinition import FunctionDefinition

class AnalyseFunctionDefinition:
    def getAllFunctionDefinitions():
        functionDefinitions = []
        for functionDefinition in FunctionDefinition.registry:
            functionDefinitions.append(functionDefinition.name)
        return functionDefinitions
    
    def getAllConstructors():
        constructors = []
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.isConstructor):
                constructors.append(functionDefinition.name)
        return constructors
    
    def getAllFunctionDefinitionsWithExternalVisibility():
        functionDefinitions = []
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.visibility == "external"):
                functionDefinitions.append(functionDefinition.name)
        return functionDefinitions

    def getAllFunctionDefinitionsWithPublicVisibility():
        functionDefinitions = []
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.visibility == "public"):
                functionDefinitions.append(functionDefinition.name)
        return functionDefinitions

    def getAllFunctionDefinitionsWithInternalVisibility():
        functionDefinitions = []
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.visibility == "internal"):
                functionDefinitions.append(functionDefinition.name)
        return functionDefinitions

    def getAllFunctionDefinitionsWithPrivateVisibility():
        functionDefinitions = []
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.visibility == "private"):
                functionDefinitions.append(functionDefinition.name)
        return functionDefinitions

    def getAllPureFunctions():
        functionDefinitions = []
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.stateMutability == "pure"):
                functionDefinitions.append(functionDefinition.name)
        return functionDefinitions

    def getAllViewFunctions():
        functionDefinitions = []
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.stateMutability == "view"):
                functionDefinitions.append(functionDefinition.name)
        return functionDefinitions

    def hasFallbackFunction():
        fallbackFunctionCount = 0 # One contract can have only one but there may be multiple contracts in the file
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.name == "" and
                len(functionDefinition.parameters["parameters"]) == 0 and
                len(functionDefinition.returnParameters["parameters"]) == 0):
                fallbackFunctionCount += 1
        return fallbackFunctionCount

    def hasPayableFallbackFunction():
        payableFallbackFunctionCount = 0 # One contract can have only one but there may be multiple contracts in the file
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.name == "" and
                len(functionDefinition.parameters["parameters"]) == 0 and
                len(functionDefinition.returnParameters["parameters"]) == 0 and
                functionDefinition.payable):
                payableFallbackFunctionCount += 1
        return payableFallbackFunctionCount

    
    
    
