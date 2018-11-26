from AnalyseAST.functionCall import AnalyseFunctionCall
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers

class AnalyseExceptions:

    statsRequires = []
    statsAsserts = []
    statsReverts = []
    
    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Exceptions >>>>>>>>>>")
        
        requires = AnalyseFunctionCall.getAllRequires()
        print("Number of require(): " + str(len(requires)))
        for require in requires:
            print("require() " + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(require.src.split(":",)[0]))))
            self.statsRequires.append({
                "line":str(mapASTSourceToLineNumbers.getLine(int(require.src.split(":",)[0]))),
                "info":"require"
            })

        asserts = AnalyseFunctionCall.getAllAsserts()
        print("Number of assert(): " + str(len(asserts)))
        for _assert in asserts:
            print("assert() " + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(_assert.src.split(":",)[0]))))
            self.statsAsserts.append({
                "line":str(mapASTSourceToLineNumbers.getLine(int(_assert.src.split(":",)[0]))),
                "info":"assert"
            })

        reverts = AnalyseFunctionCall.getAllReverts()
        print("Number of revert(): " + str(len(reverts)))
        for revert in reverts:
            print("revert() " + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(revert.src.split(":",)[0]))))
            self.statsReverts.append({
                "line":str(mapASTSourceToLineNumbers.getLine(int(revert.src.split(":",)[0]))),
                "info":"revert"
            })

