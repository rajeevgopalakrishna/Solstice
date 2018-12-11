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

class AnalyseContractFeatures:

    statsContractDefinitions = []
    statsFunctionDefinitions = []
    statsConstructors = []
    statsVariableDeclarations = []
    statsFallbackFunctions = []
    statsStateVariables = []
    
    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Contract Features >>>>>>>>>>")
        
        contracts = AnalyseContract.getAllContracts()
        for contract in contracts:
            self.statsContractDefinitions.append({
                "line":str(mapASTSourceToLineNumbers.getLine(int(contract.src.split(":",)[0]))),
                "info":"contract definition"
            })
            print("\n********** Contract Features **********")
            print("Contract definition: " + contract.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(contract.src.split(":",)[0]))))
        
        functionDefinitions = AnalyseFunctionDefinition.getAllFunctionDefinitions()
        for function in functionDefinitions:
            self.statsFunctionDefinitions.append({
                "line":str(mapASTSourceToLineNumbers.getLine(int(function.src.split(":",)[0]))),
                "info":"function definition"
            })
            print("\n********** Function Features **********")
            print("Function definition: " + function.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(function.src.split(":",)[0]))))
            if (function.isConstructor):
                self.statsConstructors.append({
                    "line":str(mapASTSourceToLineNumbers.getLine(int(function.src.split(":",)[0]))),
                    "info":"constructor definition"
                })
                print("Constructor")
            print("Visibility: " + function.visibility)
            print("State Mutability: " + function.stateMutability)
            if (AnalyseFunctionDefinition.isFallbackFunction(function)):
                self.statsFallbackFunctions.append({
                    "line":str(mapASTSourceToLineNumbers.getLine(int(function.src.split(":",)[0]))),
                    "info":"fallback definition"
                })
                print("Fallback function")
            if (AnalyseFunctionDefinition.isPayableFallbackFunction(function)):
                print("Payable Fallback function")
            modifiers = function.modifiers
            for modifier in modifiers:
                print("Modifier: " + modifier['modifierName']['name'])
                    
        variableDeclarations = AnalyseVariable.getAllVariables()
        for variable in variableDeclarations:
            self.statsVariableDeclarations.append({
                "line":str(mapASTSourceToLineNumbers.getLine(int(variable.src.split(":",)[0]))),
                "info":"variable declaration"
            })
            print("\n********** Variable Features **********")
            print("Variable declaration: " + variable.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(variable.src.split(":",)[0]))))
            if (variable.stateVariable):
                self.statsStateVariables.append({
                    "line":str(mapASTSourceToLineNumbers.getLine(int(variable.src.split(":",)[0]))),
                    "info":"state variable declaration"
                })
                print("State variable")
            else:
                if (variable.parent.nodeType == "FunctionDefinition"):
                    print("Function parameter")
                else:
                    print("Local variable")
