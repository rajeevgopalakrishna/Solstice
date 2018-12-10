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

from ParseAST.expression import Expression

class AnalyseExpression:
    def getAllExpressions():
        return Expression.registry
    
    def getAllTransfers():
        transfers = [] 
        for expression in Expression.registry:
            if (expression.memberName == "transfer"):
                transfers.append(expression)
        return transfers

    def getAllSends():
        sends = [] 
        for expression in Expression.registry:
            if (expression.memberName == "send"):
                sends.append(expression)
        return sends

    def getAllCalls():
        calls = [] 
        for expression in Expression.registry:
            if (expression.memberName == "call"):
                calls.append(expression)
        return calls

    def getAllDelegateCalls():
        delegateCalls = [] 
        for expression in Expression.registry:
            if (expression.memberName == "delegatecall"):
                delegateCalls.append(expression)
        return delegateCalls

    def getAllTxOrigins():
        txOrigins = [] 
        for expression in Expression.registry:
            found = False
            if (expression.memberName == "origin"):
                for child in expression.children:
                    if (child.nodeType == "Identifier" and child.name == "tx"):
                        found = True
                        break
            if (found):
                txOrigins.append(expression)
        return txOrigins

    def getAllBlockMembers():
        blockMembers = [] 
        for expression in Expression.registry:
            found = False
            if (expression.memberName == "coinbase" or
                expression.memberName == "timestamp" or
                expression.memberName == "gaslimit" or
                expression.memberName == "number" or
                expression.memberName == "blockhash"
            ):
                for child in expression.children:
                    if (child.nodeType == "Identifier" and child.name == "block"):
                        found = True
                        break
                if (found):
                    blockMembers.append(expression)
        return blockMembers


    
    
    
