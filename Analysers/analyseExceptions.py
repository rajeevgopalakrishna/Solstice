from AnalyseAST.functionCall import AnalyseFunctionCall
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers

class AnalyseExceptions:

    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        
        requires = AnalyseFunctionCall.getAllRequires()
        print("Number of require()s: " + str(len(requires)))
        for require in requires:
            print("require() " + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(require.src.split(":",)[0]))))

        asserts = AnalyseFunctionCall.getAllAsserts()
        print("Number of assert()s: " + str(len(asserts)))
        for _assert in asserts:
            print("assert() " + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(_assert.src.split(":",)[0]))))

        reverts = AnalyseFunctionCall.getAllReverts()
        print("Number of revert()s: " + str(len(reverts)))
        for revert in reverts:
            print("revert() " + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(revert.src.split(":",)[0]))))
        
