from collections import defaultdict
from AnalyseAST.functionDefinition import AnalyseFunctionDefinition
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers


class AnalyseTaintedVariables:

    def analyser(self):
        
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Tainted Variables >>>>>>>>>>")
        
        externalFunctions = AnalyseFunctionDefinition.getAllFunctionDefinitionsWithExternalVisibility()
        publicFunctions = AnalyseFunctionDefinition.getAllFunctionDefinitionsWithPublicVisibility()
        taintedFunctions = externalFunctions + publicFunctions

        taintedVariables = defaultdict(list)
        for function in taintedFunctions:
            parameters = function.parameters.get("parameters")
            for parameter in parameters:
#               print("Parameter: " + str(parameter))
                taintedVariables[function.name].append(parameter)
                print("Tainted parameter: " + parameter["name"] + " of function: " + function.name)
        
        

                    
                


        
