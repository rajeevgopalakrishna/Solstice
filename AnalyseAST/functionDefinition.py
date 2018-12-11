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

from ParseAST.functionDefinition import FunctionDefinition

class AnalyseFunctionDefinition:
    def getAllFunctionDefinitions():
        functionDefinitions = []
        for functionDefinition in FunctionDefinition.registry:
            functionDefinitions.append(functionDefinition)
        return functionDefinitions
    
    def getAllConstructors():
        constructors = []
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.isConstructor):
                constructors.append(functionDefinition.name)
        return constructors
    
    def getAllFunctionDefinitionsWithExternalVisibility():
        functionDefinitions = []
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.visibility == "external"):
                functionDefinitions.append(functionDefinition)
        return functionDefinitions

    def getAllFunctionDefinitionsWithPublicVisibility():
        functionDefinitions = []
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.visibility == "public" and (functionDefinition.isConstructor == False)):
                functionDefinitions.append(functionDefinition)
        return functionDefinitions

    def getAllFunctionDefinitionsWithInternalVisibility():
        functionDefinitions = []
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.visibility == "internal"):
                functionDefinitions.append(functionDefinition)
        return functionDefinitions

    def getAllFunctionDefinitionsWithPrivateVisibility():
        functionDefinitions = []
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.visibility == "private"):
                functionDefinitions.append(functionDefinition)
        return functionDefinitions

    def getAllPureFunctions():
        functionDefinitions = []
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.stateMutability == "pure"):
                functionDefinitions.append(functionDefinition)
        return functionDefinitions

    def getAllViewFunctions():
        functionDefinitions = []
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.stateMutability == "view"):
                functionDefinitions.append(functionDefinition)
        return functionDefinitions

    def hasFallbackFunction():
        fallbackFunctionCount = 0 # One contract can have only one but there may be multiple contracts in the file
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.isConstructor == False and
                functionDefinition.name == "" and
                len(functionDefinition.parameters["parameters"]) == 0 and
                len(functionDefinition.returnParameters["parameters"]) == 0):
                fallbackFunctionCount += 1
        return fallbackFunctionCount

    def isFallbackFunction(functionDefinition):
        if (functionDefinition.isConstructor == False and
            functionDefinition.name == "" and
            len(functionDefinition.parameters["parameters"]) == 0 and
            len(functionDefinition.returnParameters["parameters"]) == 0):
            return True
        else:
            return False
        
    def hasPayableFallbackFunction():
        payableFallbackFunctionCount = 0 # One contract can have only one but there may be multiple contracts in the file
        for functionDefinition in FunctionDefinition.registry:
            if (functionDefinition.name == "" and
                len(functionDefinition.parameters["parameters"]) == 0 and
                len(functionDefinition.returnParameters["parameters"]) == 0 and
                functionDefinition.payable):
                payableFallbackFunctionCount += 1
        return payableFallbackFunctionCount

    def isPayableFallbackFunction(functionDefinition):
        if (functionDefinition.name == "" and
            len(functionDefinition.parameters["parameters"]) == 0 and
            len(functionDefinition.returnParameters["parameters"]) == 0 and
            functionDefinition.payable):
            return True
        else:
            return False
    
    
