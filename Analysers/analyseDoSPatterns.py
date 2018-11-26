from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from AnalyseAST.functionCall import AnalyseFunctionCall
from AnalyseAST.expression import AnalyseExpression

class AnalyseDoSPatterns:

    statsDoSWithUnexpectedRevert=[]
    statsDoSWithBlockGasLimit=[]
    
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
                    self.statsDoSWithBlockGasLimit.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(send.src.split(":",)[0]))),
                        "info":"send"
                    })
                    print("send() within loops are susceptible to DoS with block gas limit")
                    break
                if((node.nodeType == "FunctionCall" and node.name == "require")):
                    self.statsDoSWithUnexpectedRevert.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(send.src.split(":",)[0]))),
                        "info":"send"
                    })
                    print("Potential DoS with (unexpected) revert")
                    break
                node = node.parent
        transfers = AnalyseExpression.getAllTransfers()
        for transfer in transfers:
            print("transfer() at line:" + str(mapASTSourceToLineNumbers.getLine(int(transfer.src.split(":",)[0]))))
            node = transfer.parent
            while(node.nodeType != "ContractDefinition"):
                if(node.nodeType == "WhileStatement" or node.nodeType == "ForStatement"):
                    self.statsDoSWithBlockGasLimit.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(send.src.split(":",)[0]))),
                        "info":"transfer"
                    })
                    print("transfer() within loops are susceptible to DoS with block gas limit")
                    break
                if((node.nodeType == "FunctionCall" and node.name == "require")):
                    self.statsDoSWithUnexpectedRevert.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(send.src.split(":",)[0]))),
                        "info":"transfer"
                    })
                    print("Potential DoS with (unexpected) revert")
                    break
                node = node.parent

