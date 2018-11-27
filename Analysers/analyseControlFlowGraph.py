import logging, sys
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from AnalyseAST.functionCall import AnalyseFunctionCall
from AnalyseAST.expression import AnalyseExpression

class AnalyseControlFlowGraph:

    controlFlowGraph = []
    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Control Flow Graph >>>>>>>>>>")

        functionCalls = AnalyseFunctionCall.getAllFunctionCalls()
        for functionCall in functionCalls:
            if(functionCall.name is not None):
                print("functionCall: " + functionCall.name)
                node = functionCall.parent
                while(node.nodeType != "FunctionDefinition"):
                    node = node.parent
                self.controlFlowGraph.append({
                    "line":str(mapASTSourceToLineNumbers.getLine(int(functionCall.src.split(":",)[0]))),
                    "functionCall":functionCall.name,
                    "callerName":node.name
                })

        for item in self.controlFlowGraph:
            print(item)


        
