import logging, sys
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from AnalyseAST.functionCall import AnalyseFunctionCall
from AnalyseAST.expression import AnalyseExpression
from ParseAST.ast import AST

class AnalyseControlFlowGraph:

    controlFlowGraph = []
    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Control Flow Graph >>>>>>>>>>")

        functionCalls = AnalyseFunctionCall.getAllFunctionCalls()
        for functionCall in functionCalls:
            found = True
            if(functionCall.name is not None):
                logging.debug("functionCall: " + functionCall.name)
                node = functionCall.parent
                while(node.nodeType != "FunctionDefinition"):
                    node = node.parent
                    if (isinstance(node, AST)):
                        found = False
                        break
                if (found):
                    self.controlFlowGraph.append({
                        "callerName":node.name,
                        "calleeName":functionCall.name,
                        "line":str(mapASTSourceToLineNumbers.getLine(int(functionCall.src.split(":",)[0])))
                    })

        for item in self.controlFlowGraph:
            print(item)


        
