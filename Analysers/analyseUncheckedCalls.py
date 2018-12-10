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

from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from AnalyseAST.functionCall import AnalyseFunctionCall
from AnalyseAST.expression import AnalyseExpression

class AnalyseUncheckedCalls:

    statsUncheckedCalls = []
    statsAssertCheckedCalls = []
    statsConditionalCheckedCalls = []
    
    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Unchecked Calls >>>>>>>>>>")

        calls = AnalyseExpression.getAllCalls()
        for call in calls:
            print("call() at line:" + str(mapASTSourceToLineNumbers.getLine(int(call.src.split(":",)[0]))))
            node = call.parent
            checked = False
            while(node.nodeType != "ContractDefinition"):
                if(node.nodeType == "FunctionCall" and (node.name == "assert" or node.name == "require")):
                    self.statsAssertCheckedCalls.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(call.src.split(":",)[0]))),
                        "info":"assert checked call"
                    })
                    print("call checked with assert() or require()")
                    checked = True
                    break
                if((node.nodeType == "UnaryOperation" or node.nodeType == "BinaryOperation") and node.type == "ifStatementCondition"):
                    self.statsConditionalCheckedCalls.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(call.src.split(":",)[0]))),
                        "info":"conditional checked call"
                    })
                    print("call checked with conditional if()")
                    checked = True
                    break
                node = node.parent
            if(checked):
                continue
            else:
                self.statsUncheckedCalls.append({
                    "line":str(mapASTSourceToLineNumbers.getLine(int(call.src.split(":",)[0]))),
                    "info":"Unchecked call"
                })
                print("Unchecked call()")


