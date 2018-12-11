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

from AnalyseAST.expression import AnalyseExpression
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers

class AnalyseExternalContractInteractions:
    statsCalls = []
    statsTransfers = []
    statsSends = []
    statsDelegateCalls = []
    
    def analyser(self):
        expressions = AnalyseExpression.getAllExpressions()
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: External Contract Interactions >>>>>>>>>>")
        
        transfers = AnalyseExpression.getAllTransfers()
        for transfer in transfers:
            for child in transfer.children:
                if (child.nodeType == "Identifier"):
                    self.statsTransfers.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))),
                        "info":"transfer"
                    })
                    print("Transfer to " + child.name + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))))

        sends = AnalyseExpression.getAllSends()
        for send in sends:
            for child in send.children:
                if (child.nodeType == "Identifier"):
                    self.statsSends.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))),
                        "info":"send"
                    })
                    print("Send to " + child.name + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))))
                    
        calls = AnalyseExpression.getAllCalls()
        for call in calls:
            for child in call.children:
                if (child.nodeType == "Identifier"):
                    self.statsCalls.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))),
                        "info":"call"
                    })
                    print("Call to " + child.name + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))))

        delegateCalls = AnalyseExpression.getAllDelegateCalls()
        for delegateCall in delegateCalls:
            for child in delegateCall.children:
                if (child.nodeType == "Identifier"):
                    self.statsDelegateCalls.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))),
                        "info":"delegateCall"
                    })
                    print("DelegateCall to " + child.name + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(child.src.split(":",)[0]))))

