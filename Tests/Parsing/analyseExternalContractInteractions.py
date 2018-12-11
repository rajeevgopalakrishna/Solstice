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

import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.expression import AnalyseExpression
class TestExternalContractInteractions(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/externalContractInteractions.ast","w")
        errFD = open("./tests/externalContractInteractions.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/externalContractInteractions.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/externalContractInteractions.ast','./tests/externalContractInteractions.err'])
        p.wait()
        
    def test_externalContractInteractions(self):
        parseAST = ParseAST()
        astFD = open("./tests/externalContractInteractions.ast","r")
        parseResults = parseAST.parse(astFD)
        expressions = AnalyseExpression.getAllExpressions()
        print("Number of expressions: " + str(len(expressions)))
        transfers = AnalyseExpression.getAllTransfers()
        self.assertEqual(len(transfers), 1)
        for transfer in transfers:
            print("Transfer node:" + str(transfer))
            print("Transfer nodeType:" + transfer.nodeType)
            print("Number of children:" + str(len(transfer.children)))
            for child in transfer.children:
                print("Child of Transfer" + str(child))
                print("Child nodeType: " + child.nodeType)
                if (child.nodeType == "Identifier"):
                    print("transfer call to " + child.name)
        sends = AnalyseExpression.getAllSends()
        self.assertEqual(len(sends), 1)
        calls = AnalyseExpression.getAllCalls()
        self.assertEqual(len(calls), 1)
        delegateCalls = AnalyseExpression.getAllDelegateCalls()
        self.assertEqual(len(delegateCalls), 1)
#       staticCalls = AnalyseExpression.getAllStaticCalls()
#       self.assertEqual(len(staticCalls), 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
