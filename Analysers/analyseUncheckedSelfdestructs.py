from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from AnalyseAST.functionCall import AnalyseFunctionCall
from AnalyseAST.expression import AnalyseExpression

class AnalyseUncheckedSelfDestructs:

    statsUncheckedSelfDestructs = []
    statsConditionalCheckedSelfDestructs = []
    
    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Unchecked Selfdestructs >>>>>>>>>>")

        functionCalls = AnalyseFunctionCall.getAllFunctionCalls()
        for functionCall in functionCalls:
            if (functionCall.name == "selfdestruct"):
                print("selfdestruct() at line:" + str(mapASTSourceToLineNumbers.getLine(int(functionCall.src.split(":",)[0]))))
                node = functionCall.parent
                checked = False
                while(node.nodeType != "ContractDefinition"):
                    if(node.nodeType == "IfStatement"): # Add check for ifStatementCondition containing ownership check via msg.sender
                        self.statsConditionalCheckedSelfDestructs.append({
                            "line":str(mapASTSourceToLineNumbers.getLine(int(functionCall.src.split(":",)[0]))),
                            "info":"conditional checked selfdestruct"
                        })
                        print("selfdestruct likely checked with conditional if()")
                        checked = True
                        break
                    # Add check for Function Definition containing ownership check in a modifer via msg.sender
                    node = node.parent
                if(checked):
                    continue
                else:
                    self.statsUncheckedSelfDestructs.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(functionCall.src.split(":",)[0]))),
                        "info":"Unchecked selfdestruct"
                    })
                    print("Unchecked selfdestruct()")