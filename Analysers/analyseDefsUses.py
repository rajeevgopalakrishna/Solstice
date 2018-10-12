from AnalyseAST.contract import AnalyseContract
from AnalyseAST.functionDefinition import AnalyseFunctionDefinition
from AnalyseAST.defUse import DefUseAnalysis
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from AnalyseAST.variable import AnalyseVariable

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


        for function in functionDefinitions:
            print("\n********** Function Dataflow **********")
            print("Function definition: " + function.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(function.src.split(":",)[0]))))
            dataflow = []
            dataflow = DefUseAnalysis.getDataflowForFunction(function)
#            print(str(dataflow))
            for item in dataflow:
                _gen = []
                _kill = []
                _in = []
                _out = []
                for var in item["gen"]:
                    _gen.append(AnalyseVariable.getVariableNameForId(var))
                for var in item["kill"]:
                    _kill.append(AnalyseVariable.getVariableNameForId(var))
                for var in item["in"]:
                    _in.append(AnalyseVariable.getVariableNameForId(var))
                for var in item["out"]:
                    _out.append(AnalyseVariable.getVariableNameForId(var))
                print("Node Id: " +
                      str(item["id"]) + 
                      " at line:" +
                      str(mapASTSourceToLineNumbers.getLine(int(item["src"].split(":",)[0]))) +
                      " gen: " + str(_gen) +
                      " kill: " + str(_kill) +
                      " in: " + str(_in) +
                      " out: " + str(_out)
                )
                   


            
    
                    
