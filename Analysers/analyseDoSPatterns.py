from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from AnalyseAST.functionCall import AnalyseFunctionCall
from AnalyseAST.expression import AnalyseExpression

class AnalyseDoSPatterns:

    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: DoS Patterns >>>>>>>>>>")

        print("\n********** DoS Patterns with send()/transfer() **********")
        sends = AnalyseExpression.getAllSends()
        for send in sends:
            print("send() at line:" + str(mapASTSourceToLineNumbers.getLine(int(send.src.split(":",)[0]))))
            node = send.parent
            while(node.nodeType != "ContractDefinition"):
                if(node.nodeType == "WhileStatement" or node.nodeType == "ForStatement"):
                    print("send() within loops are susceptible to DoS with block gas limit")
                    break
                if((node.nodeType == "FunctionCall" and node.name == "require")):
                    print("Potential DoS with (unexpected) revert")
                    break
                node = node.parent
        transfers = AnalyseExpression.getAllTransfers()
        for transfer in transfers:
            print("transfer() at line:" + str(mapASTSourceToLineNumbers.getLine(int(transfer.src.split(":",)[0]))))
            node = transfer.parent
            while(node.nodeType != "ContractDefinition"):
                if(node.nodeType == "WhileStatement" or node.nodeType == "ForStatement"):
                    print("transfer() within loops are susceptible to DoS with block gas limit")
                    break
                if((node.nodeType == "FunctionCall" and node.name == "require")):
                    print("Potential DoS with (unexpected) revert")
                    break
                node = node.parent

