from AnalyseAST.contract import AnalyseContract
from AnalyseAST.functionDefinition import AnalyseFunctionDefinition
from AnalyseAST.defUse import DefUseAnalysis
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from AnalyseAST.variable import AnalyseVariable
from Libraries.myset import MySet

class AnalyseDefsUses:

    loggingLevel = "INFO"
    statsDefs = []
    statsUses = []
    
    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Defs and Uses >>>>>>>>>>")
        
        functionDefinitions = AnalyseFunctionDefinition.getAllFunctionDefinitions()

        for function in functionDefinitions:
            print("\n********** Function Defs/Uses **********")
            print("Function definition: " + function.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(function.src.split(":",)[0]))))
            dataflow = DefUseAnalysis.getDataflowForFunction(function)
            if (self.loggingLevel == "DEBUG"):
                print("Dataflow length: " + str(len(dataflow)))
                for item in dataflow:
                    _gen = []
                    _kill = []
                    _in = MySet()
                    _out = []
                    if(item["gen"] is not None and item["gen"]._set is not None):
                        for var in item["gen"]._set:
                            if(AnalyseVariable.getVariableNameForId(var) != "Error"):
                                _gen.append(AnalyseVariable.getVariableNameForId(var))
                    if(item["kill"] is not None):
                        for var in item["kill"]._set:
                            if(AnalyseVariable.getVariableNameForId(var) != "Error"):
                                _kill.append(AnalyseVariable.getVariableNameForId(var))
                    if(item["in"] is not None):
                        for var in item["in"]._set:
                            if(AnalyseVariable.getVariableNameForId(var) != "Error"):
                                _in.add(AnalyseVariable.getVariableNameForId(var), item["in"].idToNodeMapping[var].src)
                    if(item["out"] is not None):
                        for var in item["out"]._set:
                            if(AnalyseVariable.getVariableNameForId(var) != "Error"):
                                _out.append(AnalyseVariable.getVariableNameForId(var))
                    print("Node Id: " +
                          str(item["id"]) + 
                          " at line:" +
                          str(mapASTSourceToLineNumbers.getLine(int(item["src"].split(":",)[0]))) +
                          " gen: " + str(_gen) +
                          " kill: " + str(_kill)
                    )
                
                    for var in _in._set:
                        print("in: " + var + " defined at line:" + str(mapASTSourceToLineNumbers.getLine(int(_in.idToNodeMapping[var].split(":",)[0]))))
                    print(" out: " + str(_out))


            defs = []
            defs = DefUseAnalysis.getAllDefsAtNode(function, defs)
            
            for _def in defs:
                self.statsDefs.append({
                    "line":str(mapASTSourceToLineNumbers.getLine(int(_def["src"].split(":",)[0]))),
                    "info":_def["name"]
                })
                if(self.loggingLevel == "DEBUG"):
                    print("Def: " + _def["name"] + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(_def["src"].split(":",)[0]))))
            
            uses = []
            uses = DefUseAnalysis.getAllUsesAtNode(function, uses)
            for use in uses:
                self.statsUses.append({
                    "line":str(mapASTSourceToLineNumbers.getLine(int(use["src"].split(":",)[0]))),
                    "info":use["name"]
                })
                print("Use: " +
                      use["name"] +
                      " at line:" + str(mapASTSourceToLineNumbers.getLine(int(use["src"].split(":",)[0]))))
                print(" > Using value from definition on line: ",end='')
                line = mapASTSourceToLineNumbers.getLine(int(use["src"].split(":",)[0]))
                varRef = use["referencedDeclaration"]
                found = False
                for item in dataflow:
                    if(mapASTSourceToLineNumbers.getLine(int(item["src"].split(":",)[0])) == line):
                        if(item["in"] and varRef in item["in"]._set):
                            print(mapASTSourceToLineNumbers.getLine(int(item["in"].idToNodeMapping[varRef].src.split(":",)[0])))
                            found = True
                            break
                if(not found):
                    print("Not Found")
                    
