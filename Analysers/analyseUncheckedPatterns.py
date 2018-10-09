from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from AnalyseAST.functionCall import AnalyseFunctionCall
from AnalyseAST.expression import AnalyseExpression

class AnalyseUncheckedPatterns:

    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Unchecked Patterns >>>>>>>>>>")

        print("\n********** Unchecked call() **********")
        calls = AnalyseExpression.getAllCalls()
        for call in calls:
            print("call() at line:" + str(mapASTSourceToLineNumbers.getLine(int(call.src.split(":",)[0]))))
            node = call.parent
            checked = False
            while(node.nodeType != "ContractDefinition"):
                if(node.nodeType == "FunctionCall" and node.name == "assert"):
                    print("call checked with assert()")
                    checked = True
                    break
                if((node.nodeType == "UnaryOperation" or node.nodeType == "BinaryOperation") and node.type == "ifStatementCondition"):
                    print("call checked with conditional if()")
                    checked = True
                    break
                node = node.parent
            if(checked):
                continue
            else:
                print("Unchecked call()")
