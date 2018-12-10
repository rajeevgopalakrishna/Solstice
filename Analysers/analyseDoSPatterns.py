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

class AnalyseDoSPatterns:

    statsDoSWithUnexpectedRevert=[]
    statsDoSWithBlockGasLimit=[]
    
    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: DoS Patterns >>>>>>>>>>")

        print("\n********** DoS Patterns with send()/transfer() **********")
        sends = AnalyseExpression.getAllSends()
        for send in sends:
            print("send() at line:" + str(mapASTSourceToLineNumbers.getLine(int(send.src.split(":",)[0]))))
            node = send.parent
            while(node.nodeType != "ContractDefinition"):
                if(node.nodeType == "WhileStatement" or node.nodeType == "ForStatement"):
                    self.statsDoSWithBlockGasLimit.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(send.src.split(":",)[0]))),
                        "info":"send"
                    })
                    print("send() within loops are susceptible to DoS with block gas limit")
                    break
                if((node.nodeType == "FunctionCall" and node.name == "require")):
                    self.statsDoSWithUnexpectedRevert.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(send.src.split(":",)[0]))),
                        "info":"send"
                    })
                    print("Potential DoS with (unexpected) revert")
                    break
                node = node.parent
        transfers = AnalyseExpression.getAllTransfers()
        for transfer in transfers:
            print("transfer() at line:" + str(mapASTSourceToLineNumbers.getLine(int(transfer.src.split(":",)[0]))))
            node = transfer.parent
            while(node.nodeType != "ContractDefinition"):
                if(node.nodeType == "WhileStatement" or node.nodeType == "ForStatement"):
                    self.statsDoSWithBlockGasLimit.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(transfer.src.split(":",)[0]))),
                        "info":"transfer"
                    })
                    print("transfer() within loops are susceptible to DoS with block gas limit")
                    break
                if((node.nodeType == "FunctionCall" and node.name == "require")):
                    self.statsDoSWithUnexpectedRevert.append({
                        "line":str(mapASTSourceToLineNumbers.getLine(int(transfer.src.split(":",)[0]))),
                        "info":"transfer"
                    })
                    print("Potential DoS with (unexpected) revert")
                    break
                node = node.parent

