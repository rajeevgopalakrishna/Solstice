#	Copyright (c) 2018 Rajeev Gopalakrishna
#
#	This file is part of Solstice.
#
#	Solstice is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	Solstice is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with Solstice.  If not, see <http://www.gnu.org/licenses/>.

from ParseAST.functionCall import FunctionCall

class AnalyseFunctionCall:
    def getAllFunctionCalls():
        functionCalls = []
        for functionCall in FunctionCall.registry:
            functionCalls.append(functionCall)
        return functionCalls

    def getAllFunctionCallNames():
        functionCalls = []
        for functionCall in FunctionCall.registry:
            functionCalls.append(functionCall.name)
        return functionCalls

    def getAllRequires():
        requires = []
        for functionCall in FunctionCall.registry:
            if(functionCall.name == "require"):
                requires.append(functionCall)
        return requires

    def getAllAsserts():
        asserts = []
        for functionCall in FunctionCall.registry:
            if(functionCall.name == "assert"):
                asserts.append(functionCall)
        return asserts

    def getAllReverts():
        reverts = []
        for functionCall in FunctionCall.registry:
            if(functionCall.name == "revert"):
                reverts.append(functionCall)
        return reverts
