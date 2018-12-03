import logging, sys
from collections import defaultdict
from AnalyseAST.functionDefinition import AnalyseFunctionDefinition
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from AnalyseAST.defUse import DefUseAnalysis
from AnalyseAST.taintPropagate import TaintPropagate
from AnalyseAST.variable import AnalyseVariable
from Libraries.myset import MySet

class AnalyseTaintedVariables:
    statsTaintedVariables = []
    
    def analyser(self):
        
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Tainted Variables >>>>>>>>>>")
        
        externalFunctions = AnalyseFunctionDefinition.getAllFunctionDefinitionsWithExternalVisibility()
        publicFunctions = AnalyseFunctionDefinition.getAllFunctionDefinitionsWithPublicVisibility()
        taintedFunctions = externalFunctions + publicFunctions

        taintedVariables = defaultdict(list)
        for function in taintedFunctions:
            taintFlow = TaintPropagate.getTaintPropagationForFunction(function)            
            for item in taintFlow:
                _in = MySet()
                _out = []
                if(item["in"] is not None):
                    for var in item["in"]._set:
                        if(AnalyseVariable.getVariableNameForId(var) != "Error"):
                            _in.add(AnalyseVariable.getVariableNameForId(var), item["in"].idToNodeMapping[var].src)
                if(item["out"] is not None):
                    for var in item["out"]._set:
                        if(AnalyseVariable.getVariableNameForId(var) != "Error"):
                            _out.append(AnalyseVariable.getVariableNameForId(var))

                print("At line: " + str(mapASTSourceToLineNumbers.getLine(int(item["src"].split(":",)[0]))))

                for var in _in._set:
                    print(" Incoming tainted variable: " + var + " defined at line:" + str(mapASTSourceToLineNumbers.getLine(int(_in.idToNodeMapping[var].split(":",)[0]))))
                print(" Outgoing tainted variables: " + str(_out))
                self.statsTaintedVariables.append({
                    "line":str(mapASTSourceToLineNumbers.getLine(int(item["src"].split(":",)[0]))),
                    "info":_out,
                })

                


        
