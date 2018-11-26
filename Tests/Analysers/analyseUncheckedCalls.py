import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from Analysers.analyseUncheckedCalls import AnalyseUncheckedCalls

class TestUncheckedCalls(unittest.TestCase):

    testFile = "uncheckedCalls"
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
        analyseUncheckedCalls = AnalyseUncheckedCalls()
        analyseUncheckedCalls.analyser()
        self.assertEqual(len(analyseUncheckedCalls.statsAssertCheckedCalls), 1)
        self.assertEqual(analyseUncheckedCalls.statsAssertCheckedCalls[0]["line"], "6")
        self.assertEqual(len(analyseUncheckedCalls.statsConditionalCheckedCalls), 2)
        self.assertEqual(analyseUncheckedCalls.statsConditionalCheckedCalls[0]["line"], "10")
        self.assertEqual(analyseUncheckedCalls.statsConditionalCheckedCalls[1]["line"], "13")
        self.assertEqual(len(analyseUncheckedCalls.statsUncheckedCalls), 1)
        self.assertEqual(analyseUncheckedCalls.statsUncheckedCalls[0]["line"], "19")
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
