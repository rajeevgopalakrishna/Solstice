import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from Analysers.analyseExceptions import AnalyseExceptions

class TestExceptions(unittest.TestCase):

    testFile = "exceptions"
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
        analyseExceptions = AnalyseExceptions()
        analyseExceptions.analyser()
        self.assertEqual(len(analyseExceptions.statsRequires), 1)
        self.assertEqual(analyseExceptions.statsRequires[0]["line"], "9")
        self.assertEqual(len(analyseExceptions.statsAsserts), 1)
        self.assertEqual(analyseExceptions.statsAsserts[0]["line"], "11")
        self.assertEqual(len(analyseExceptions.statsReverts), 1)
        self.assertEqual(analyseExceptions.statsReverts[0]["line"], "13")
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
