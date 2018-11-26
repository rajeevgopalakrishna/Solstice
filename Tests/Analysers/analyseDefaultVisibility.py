import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from Analysers.analyseDefaultVisibility import AnalyseDefaultVisibility

class TestDefaultVisibility(unittest.TestCase):

    testFile = "defaultVisibility"
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
        analyseDefaultVisibility = AnalyseDefaultVisibility()
        analyseDefaultVisibility.analyser()
        self.assertEqual(len(analyseDefaultVisibility.statsDefaultVisibilityForFunction), 1)
        self.assertEqual(analyseDefaultVisibility.statsDefaultVisibilityForFunction[0]["line"], "8")
        self.assertEqual(len(analyseDefaultVisibility.statsDefaultVisibilityForVariable), 1)
        self.assertEqual(analyseDefaultVisibility.statsDefaultVisibilityForVariable[0]["line"], "5")
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
