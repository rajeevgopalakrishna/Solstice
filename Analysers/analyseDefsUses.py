from AnalyseAST.contract import AnalyseContract
from AnalyseAST.functionDefinition import AnalyseFunctionDefinition
from AnalyseAST.defUse import DefUseAnalysis
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers

class AnalyseDefsUses:

    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Defs and Uses >>>>>>>>>>")
        
        functionDefinitions = AnalyseFunctionDefinition.getAllFunctionDefinitions()
        for function in functionDefinitions:
            print("\n********** Function Defs/Uses **********")
            print("Function definition: " + function.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(function.src.split(":",)[0]))))
            defs = []
            defs = DefUseAnalysis.getAllDefsAtNode(function, defs)
            for _def in defs:
                print("Def: " + _def["name"] + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(_def["src"].split(":",)[0]))))
            uses = []
            uses = DefUseAnalysis.getAllUsesAtNode(function, uses)
            for use in uses:
                print("Use: " + use["name"] + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(use["src"].split(":",)[0]))))

            
    
                    
