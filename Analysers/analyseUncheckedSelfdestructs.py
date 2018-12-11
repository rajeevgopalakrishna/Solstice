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

from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from AnalyseAST.functionCall import AnalyseFunctionCall
from AnalyseAST.expression import AnalyseExpression

class AnalyseUncheckedSelfdestructs:

    statsUncheckedSelfdestructs = []
    statsConditionalCheckedSelfdestructs = []
    
    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Unchecked Selfdestructs >>>>>>>>>>")

        functionCalls = AnalyseFunctionCall.getAllFunctionCalls()
        for functionCall in functionCalls:
            if (functionCall.name == "selfdestruct"):
                print("selfdestruct() at line:" + str(mapASTSourceToLineNumbers.getLine(int(functionCall.src.split(":",)[0]))))
                node = functionCall.parent
                checked = False
                while(node.nodeType != "ContractDefinition"):
                    if(node.nodeType == "IfStatement"): # Add check for ifStatementCondition containing ownership check via msg.sender
                        self.statsConditionalCheckedSelfdestructs.append({
                            "line":str(mapASTSourceToLineNumbers.getLine(int(functionCall.src.split(":",)[0]))),
                            "info":"conditional checked selfdestruct"
                        })
                        print("selfdestruct likely checked with conditional if()")
                        checked = True
                        break
                    # Add check for Function Definition containing ownership check in a modifer via msg.sender
                    node = node.parent
                if(checked):
                    continue
                else:
                    self.statsUncheckedSelfdestructs.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(functionCall.src.split(":",)[0]))),
                        "info":"Unchecked selfdestruct"
                    })
                    print("Unchecked selfdestruct()")
