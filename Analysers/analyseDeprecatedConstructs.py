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
from AnalyseAST.expression import AnalyseExpression

class AnalyseDeprecatedConstructs:

    statsTxOrigin = []
    statsBlockMembers = []
    
    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Unchecked Deprecated Constructs >>>>>>>>>>")

        print("\n********** Use of tx.origin **********")
        constructs = AnalyseExpression.getAllTxOrigins()
        for construct in constructs:
            self.statsTxOrigin.append({
                "line":str(mapASTSourceToLineNumbers.getLine(int(construct.src.split(":",)[0]))),
                "info":"tx.origin"
            })
            print("tx.origin at line:" + str(mapASTSourceToLineNumbers.getLine(int(construct.src.split(":",)[0]))))


        print("\n********** Use of block.<member> where member is number/hash/gaslimit/coinbase/timestamp **********")
        constructs = AnalyseExpression.getAllBlockMembers()
        for construct in constructs:
            self.statsBlockMembers.append({
                "line":str(mapASTSourceToLineNumbers.getLine(int(construct.src.split(":",)[0]))),
                "info":"block.<member>"
            })
            print("Predictable block member at line:" + str(mapASTSourceToLineNumbers.getLine(int(construct.src.split(":",)[0]))))

