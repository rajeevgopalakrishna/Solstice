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

import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.functionCall import AnalyseFunctionCall

class TestFunctionCallAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/functionCall.ast","w")
        errFD = open("./tests/functionCall.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/functionCall.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/functionCall.ast','./tests/functionCall.err'])
        p.wait()
        
    def test_functionCall(self):
        parseAST = ParseAST()
        astFD = open("./tests/functionCall.ast","r")
        parseResults = parseAST.parse(astFD)
        self.assertEqual(parseResults['Counts']['FunctionCallCount'], 1)
        functionCalls = AnalyseFunctionCall.getAllFunctionCalls()
        self.assertEqual(len(functionCalls), 1)
        self.assertEqual(functionCalls[0],"foo")
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
