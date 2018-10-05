from ParseAST.functionCall import FunctionCall

class AnalyseFunctionCall:
    def getAllFunctionCalls():
        functionCalls = []
        for functionCall in FunctionCall.registry:
            functionCalls.append(functionCall.name)
        return functionCalls
