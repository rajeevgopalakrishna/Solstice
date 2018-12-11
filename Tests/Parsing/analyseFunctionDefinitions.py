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
from AnalyseAST.functionDefinition import AnalyseFunctionDefinition
class TestFunctionDefinitions(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/functionDefinition.ast","w")
        errFD = open("./tests/functionDefinition.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/functionDefinition.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/functionDefinitions.ast','./tests/functionDefinitions.err'])
        p.wait()
        
    def test_functionDefinition(self):
        parseAST = ParseAST()
        astFD = open("./tests/functionDefinition.ast","r")
        parseResults = parseAST.parse(astFD)
        functionDefinitions = AnalyseFunctionDefinition.getAllFunctionDefinitions()
        for item in functionDefinitions:
            print("Function Definition Name: " + item)
        self.assertEqual(len(functionDefinitions), 2)
        functionDefinitionsPublicVisibility = AnalyseFunctionDefinition.getAllFunctionDefinitionsWithPublicVisibility()
        for item in functionDefinitionsPublicVisibility:
            print("Public Function Definition Name: " + item)
        self.assertEqual(len(functionDefinitionsPublicVisibility), 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
