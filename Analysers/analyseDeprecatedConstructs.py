from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from AnalyseAST.expression import AnalyseExpression

class AnalyseDeprecatedConstructs:

    statsTxOrigin = []
    statsBlockMembers = []
    
    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Unchecked Deprecated Constructs >>>>>>>>>>")

        print("\n********** Use of tx.origin **********")
        constructs = AnalyseExpression.getAllTxOrigins()
        for construct in constructs:
            self.statsTxOrigin.append({
                "line":str(mapASTSourceToLineNumbers.getLine(int(construct.src.split(":",)[0]))),
                "info":"tx.origin"
            })
            print("tx.origin at line:" + str(mapASTSourceToLineNumbers.getLine(int(construct.src.split(":",)[0]))))


        print("\n********** Use of block.<member> where member is number/hash/gaslimit/coinbase/timestamp **********")
        constructs = AnalyseExpression.getAllBlockMembers()
        for construct in constructs:
            self.statsBlockMembers.append({
                "line":str(mapASTSourceToLineNumbers.getLine(int(construct.src.split(":",)[0]))),
                "info":"block.<member>"
            })
            print("Predictable block member at line:" + str(mapASTSourceToLineNumbers.getLine(int(construct.src.split(":",)[0]))))

