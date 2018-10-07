from ParseAST.functionCall import FunctionCall

class AnalyseFunctionCall:
    def getAllFunctionCalls():
        functionCalls = []
        for functionCall in FunctionCall.registry:
            functionCalls.append(functionCall.name)
        return functionCalls

    def getAllRequires():
        requires = []
        for functionCall in FunctionCall.registry:
            if(functionCall.name == "require"):
                requires.append(functionCall)
        return requires

    def getAllAsserts():
        asserts = []
        for functionCall in FunctionCall.registry:
            if(functionCall.name == "assert"):
                asserts.append(functionCall)
        return asserts

    def getAllReverts():
        reverts = []
        for functionCall in FunctionCall.registry:
            if(functionCall.name == "revert"):
                reverts.append(functionCall)
        return reverts
