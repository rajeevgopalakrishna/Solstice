from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from AnalyseAST.expression import AnalyseExpression

class AnalyseDeprecatedConstructs:

    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Unchecked Deprecated Constructs >>>>>>>>>>")

        print("\n********** Use of tx.origin **********")
        constructs = AnalyseExpression.getAllTxOrigins()
        for construct in constructs:
            print("tx.origin at line:" + str(mapASTSourceToLineNumbers.getLine(int(construct.src.split(":",)[0]))))


        print("\n********** Use of block.<member> where member is number/hash/gaslimit/coinbase/timestamp **********")
        constructs = AnalyseExpression.getAllBlockMembers()
        for construct in constructs:
            print("Predictable block member at line:" + str(mapASTSourceToLineNumbers.getLine(int(construct.src.split(":",)[0]))))

