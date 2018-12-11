#    Copyright (C) 2018 Rajeev Gopalakrishna
#
#    This file is part of Solstice.
#
#    Solstice is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    Solstice is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from AnalyseAST.contract import AnalyseContract
from AnalyseAST.functionDefinition import AnalyseFunctionDefinition
from AnalyseAST.variable import AnalyseVariable
from AnalyseAST.expression import AnalyseExpression
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers

class AnalyseDefaultVisibility:

    statsDefaultVisibilityForFunction = []
    statsDefaultVisibilityForVariable = []
    
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
                    self.statsDefaultVisibilityForFunction.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(function.src.split(":",)[0]))),
                        "info":"default public visibility for function"
                    })
                    print("Default public visibility for Function: " + function.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(function.src.split(":",)[0]))))
                    
        variableDeclarations = AnalyseVariable.getAllVariables()
        for variable in variableDeclarations:
            if (variable.visibility == "internal" and (not (variable.parent.nodeType == "FunctionDefinition"))):
                # Determine if "internal" visibility was explicitly specified or implicitly inferred
                # Check if "internal" keyword is present between type and variable name
                variableSrc = variable.src
                typeSrc = variable.typeName.get("src")
                found = mapASTSourceToLineNumbers.chkStringPresentVariableVisibility("internal",typeSrc, variableSrc)
                if (not found):
                    self.statsDefaultVisibilityForVariable.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(variable.src.split(":",)[0]))),
                        "info":"default public visibility for variable"
                    })
                    print("Default internal visibility for Variable: " + variable.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(variable.src.split(":",)[0]))))
