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

import logging, sys
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from AnalyseAST.functionCall import AnalyseFunctionCall
from AnalyseAST.expression import AnalyseExpression
from ParseAST.ast import AST

class AnalyseControlFlowGraph:

    controlFlowGraph = []
    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Control Flow Graph >>>>>>>>>>")

        functionCalls = AnalyseFunctionCall.getAllFunctionCalls()
        for functionCall in functionCalls:
            found = True
            if(functionCall.name is not None):
                logging.debug("functionCall: " + functionCall.name)
                node = functionCall.parent
                while(node.nodeType != "FunctionDefinition"):
                    node = node.parent
                    if (isinstance(node, AST)):
                        found = False
                        break
                if (found):
                    self.controlFlowGraph.append({
                        "callerName":node.name,
                        "calleeName":functionCall.name,
                        "line":str(mapASTSourceToLineNumbers.getLine(int(functionCall.src.split(":",)[0])))
                    })

        for item in self.controlFlowGraph:
            print(item)


        
