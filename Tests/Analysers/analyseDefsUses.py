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
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from Analysers.analyseDefsUses import AnalyseDefsUses

class TestDefsUses(unittest.TestCase):

    testFile = "defuse"
    testDir = "./Tests/Analysers/"
    testPath = testDir+testFile

    def setUp(self):
        astFD = open(self.testPath+".ast","w")
        errFD = open(self.testPath+".err","w")
        p = subprocess.Popen(['solc','--ast-compact-json',self.testDir+'Contracts/'+self.testFile+'.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f',self.testPath+'.ast',self.testPath+'.err'])
        p.wait()
        
    def test_exceptions(self):
        parseAST = ParseAST()
        astFD = open(self.testPath+".ast","r")
        parseResults = parseAST.parse(astFD)
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        mapASTSourceToLineNumbers.analyser(self.testDir+"Contracts/"+self.testFile+".sol")
        analyseDefsUses = AnalyseDefsUses()
        analyseDefsUses.analyser()
        self.assertEqual(len(analyseDefsUses.statsDefs), 16)
        self.assertEqual(analyseDefsUses.statsDefs[0]["line"], "14")
        self.assertEqual(analyseDefsUses.statsDefs[0]["info"], "k")
        self.assertEqual(analyseDefsUses.statsDefs[1]["line"], "18")
        self.assertEqual(analyseDefsUses.statsDefs[1]["info"], "i")
        self.assertEqual(analyseDefsUses.statsDefs[2]["line"], "21")
        self.assertEqual(analyseDefsUses.statsDefs[2]["info"], "a")
        self.assertEqual(analyseDefsUses.statsDefs[3]["line"], "22")
        self.assertEqual(analyseDefsUses.statsDefs[3]["info"], "a")
        self.assertEqual(analyseDefsUses.statsDefs[4]["line"], "23")
        self.assertEqual(analyseDefsUses.statsDefs[4]["info"], "j")
        self.assertEqual(analyseDefsUses.statsDefs[5]["line"], "24")
        self.assertEqual(analyseDefsUses.statsDefs[5]["info"], "a")
        self.assertEqual(analyseDefsUses.statsDefs[6]["line"], "25")
        self.assertEqual(analyseDefsUses.statsDefs[6]["info"], "i")
        self.assertEqual(analyseDefsUses.statsDefs[7]["line"], "28")
        self.assertEqual(analyseDefsUses.statsDefs[7]["info"], "i")
        self.assertEqual(analyseDefsUses.statsDefs[8]["line"], "31")
        self.assertEqual(analyseDefsUses.statsDefs[8]["info"], "j")
        self.assertEqual(analyseDefsUses.statsDefs[9]["line"], "34")
        self.assertEqual(analyseDefsUses.statsDefs[9]["info"], "a")
        self.assertEqual(analyseDefsUses.statsDefs[10]["line"], "35")
        self.assertEqual(analyseDefsUses.statsDefs[10]["info"], "j")
        self.assertEqual(analyseDefsUses.statsDefs[11]["line"], "38")
        self.assertEqual(analyseDefsUses.statsDefs[11]["info"], "data")
        self.assertEqual(analyseDefsUses.statsDefs[12]["line"], "40")
        self.assertEqual(analyseDefsUses.statsDefs[12]["info"], "balances")
        self.assertEqual(analyseDefsUses.statsDefs[13]["line"], "40")
        self.assertEqual(analyseDefsUses.statsDefs[13]["info"], "msg")
        self.assertEqual(analyseDefsUses.statsDefs[14]["line"], "41")
        self.assertEqual(analyseDefsUses.statsDefs[14]["info"], "balances")
        self.assertEqual(analyseDefsUses.statsDefs[15]["line"], "41")
        self.assertEqual(analyseDefsUses.statsDefs[15]["info"], "i")
        
        self.assertEqual(len(analyseDefsUses.statsUses), 22)
        self.assertEqual(analyseDefsUses.statsUses[0]["line"], "15")
        self.assertEqual(analyseDefsUses.statsUses[0]["info"], "k")
        self.assertEqual(analyseDefsUses.statsUses[1]["line"], "21")
        self.assertEqual(analyseDefsUses.statsUses[1]["info"], "i")
        self.assertEqual(analyseDefsUses.statsUses[2]["line"], "22")
        self.assertEqual(analyseDefsUses.statsUses[2]["info"], "a")
        self.assertEqual(analyseDefsUses.statsUses[3]["line"], "23")
        self.assertEqual(analyseDefsUses.statsUses[3]["info"], "i")
        self.assertEqual(analyseDefsUses.statsUses[4]["line"], "24")
        self.assertEqual(analyseDefsUses.statsUses[4]["info"], "a")
        self.assertEqual(analyseDefsUses.statsUses[5]["line"], "24")
        self.assertEqual(analyseDefsUses.statsUses[5]["info"], "i")
        self.assertEqual(analyseDefsUses.statsUses[6]["line"], "24")
        self.assertEqual(analyseDefsUses.statsUses[6]["info"], "j")
        self.assertEqual(analyseDefsUses.statsUses[7]["line"], "25")
        self.assertEqual(analyseDefsUses.statsUses[7]["info"], "a")
        self.assertEqual(analyseDefsUses.statsUses[8]["line"], "25")
        self.assertEqual(analyseDefsUses.statsUses[8]["info"], "i")
        self.assertEqual(analyseDefsUses.statsUses[9]["line"], "25")
        self.assertEqual(analyseDefsUses.statsUses[9]["info"], "j")
        self.assertEqual(analyseDefsUses.statsUses[10]["line"], "25")
        self.assertEqual(analyseDefsUses.statsUses[10]["info"], "msg")
        self.assertEqual(analyseDefsUses.statsUses[11]["line"], "27")
        self.assertEqual(analyseDefsUses.statsUses[11]["info"], "a")
        self.assertEqual(analyseDefsUses.statsUses[12]["line"], "28")
        self.assertEqual(analyseDefsUses.statsUses[12]["info"], "i")
        self.assertEqual(analyseDefsUses.statsUses[13]["line"], "31")
        self.assertEqual(analyseDefsUses.statsUses[13]["info"], "bar")
        self.assertEqual(analyseDefsUses.statsUses[14]["line"], "31")
        self.assertEqual(analyseDefsUses.statsUses[14]["info"], "a")
        self.assertEqual(analyseDefsUses.statsUses[15]["line"], "31")
        self.assertEqual(analyseDefsUses.statsUses[15]["info"], "a")
        self.assertEqual(analyseDefsUses.statsUses[16]["line"], "34")
        self.assertEqual(analyseDefsUses.statsUses[16]["info"], "a")
        self.assertEqual(analyseDefsUses.statsUses[17]["line"], "35")
        self.assertEqual(analyseDefsUses.statsUses[17]["info"], "j")
        self.assertEqual(analyseDefsUses.statsUses[18]["line"], "38")
        self.assertEqual(analyseDefsUses.statsUses[18]["info"], "j")
        self.assertEqual(analyseDefsUses.statsUses[19]["line"], "40")
        self.assertEqual(analyseDefsUses.statsUses[19]["info"], "j")
        self.assertEqual(analyseDefsUses.statsUses[20]["line"], "41")
        self.assertEqual(analyseDefsUses.statsUses[20]["info"], "i")
        self.assertEqual(analyseDefsUses.statsUses[21]["line"], "41")
        self.assertEqual(analyseDefsUses.statsUses[21]["info"], "a")
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
