from AnalyseAST.expression import AnalyseExpression
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers

class AnalyseExternalContractInteractions:
    statsCalls = []
    statsTransfers = []
    statsSends = []
    statsDelegateCalls = []
    
    def analyser(self):
        expressions = AnalyseExpression.getAllExpressions()
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: External Contract Interactions >>>>>>>>>>")
        
        transfers = AnalyseExpression.getAllTransfers()
        for transfer in transfers:
            for child in transfer.children:
                if (child.nodeType == "Identifier"):
                    self.statsTransfers.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))),
                        "info":"transfer"
                    })
                    print("Transfer to " + child.name + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))))

        sends = AnalyseExpression.getAllSends()
        for send in sends:
            for child in send.children:
                if (child.nodeType == "Identifier"):
                    self.statsSends.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))),
                        "info":"send"
                    })
                    print("Send to " + child.name + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))))
                    
        calls = AnalyseExpression.getAllCalls()
        for call in calls:
            for child in call.children:
                if (child.nodeType == "Identifier"):
                    self.statsCalls.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))),
                        "info":"call"
                    })
                    print("Call to " + child.name + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))))

        delegateCalls = AnalyseExpression.getAllDelegateCalls()
        for delegateCall in delegateCalls:
            for child in delegateCall.children:
                if (child.nodeType == "Identifier"):
                    self.statsDelegateCalls.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))),
                        "info":"delegateCall"
                    })
                    print("DelegateCall to " + child.name + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))))

