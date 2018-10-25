from AnalyseAST.contract import AnalyseContract
from AnalyseAST.functionDefinition import AnalyseFunctionDefinition
from AnalyseAST.variable import AnalyseVariable
from AnalyseAST.expression import AnalyseExpression
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers

class AnalyseDefaultVisibility:

    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Default Visibility >>>>>>>>>>")
        
        functionDefinitions = AnalyseFunctionDefinition.getAllFunctionDefinitions()
        for function in functionDefinitions:
            if (function.visibility == "public"):
                # Determine if "public" visibility was explicitly specified or implicitly inferred
                # Check if "public" keyword is present between input parameters and return parameters
                parametersSrc = function.parameters.get("src")
                returnParametersSrc = function.returnParameters.get("src")
                found = mapASTSourceToLineNumbers.chkStringPresent("public",parametersSrc, returnParametersSrc)
                if (not found):
                    print("Default public visibility for Function: " + function.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(function.src.split(":",)[0]))))
                    
        variableDeclarations = AnalyseVariable.getAllVariables()
        for variable in variableDeclarations:
            if (variable.visibility == "internal"):
                # Determine if "internal" visibility was explicitly specified or implicitly inferred
                # Check if "internal" keyword is present between type and variable name
                variableSrc = variable.src
                typeSrc = variable.typeName.get("src")
                found = mapASTSourceToLineNumbers.chkStringPresentVariableVisibility("internal",typeSrc, variableSrc)
                if (not found):
                    print("Default internal visibility for Variable: " + variable.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(variable.src.split(":",)[0]))))
