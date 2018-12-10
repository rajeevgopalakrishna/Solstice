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
from AnalyseAST.expression import AnalyseExpression
from AnalyseAST.variable import AnalyseVariable
from AnalyseAST.defUse import DefUseAnalysis
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers


class AnalyseReentrancy:

    statsPotentialReentrancy = []
    
    def analyser(self):
        expressions = AnalyseExpression.getAllExpressions()
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Reentrancy >>>>>>>>>>")
        
        calls = AnalyseExpression.getAllCalls()
        for call in calls:
            logging.debug("Call at line:" + str(mapASTSourceToLineNumbers.getLine(int(call.src.split(":",)[0]))))
            parent = call.parent
            found = False
            defs = []
            while(True):
                if (parent.nodeType == "ExpressionStatement"):
                    logging.debug("Found ExpressionStatement: " + str(parent.id))
                    found = True
                    break
                if (parent.nodeType == "ContractDefinition"):
                    break
                parent = parent.parent
            if (found):
                defs = DefUseAnalysis.getAllDefintionsAfterStatement(parent)
            defsOfStateVariables = []
            for _def in defs:
                logging.debug("_def: " + str(_def))
                logging.debug("Def: " + _def["name"] + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(_def["src"].split(":",)[0]))))
                variableID = _def["referencedDeclaration"]
                variables = AnalyseVariable.getAllVariables()
                for variable in variables:
                    if (variableID == variable.id and variable.stateVariable):
                        defsOfStateVariables.append(_def)
            if (len(defsOfStateVariables) != 0):
                self.statsPotentialReentrancy.append({
                    "line":str(mapASTSourceToLineNumbers.getLine(int(call.src.split(":",)[0]))),
                    "info":"potential reentrancy: state change after call()"
                })
                print("Potential Reentrancy: State change after call()")
            else:
                print("No Reentrancy: No state change after call()")

                    
                


        
