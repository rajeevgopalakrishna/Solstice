import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from Analysers.analyseDoSPatterns import AnalyseDoSPatterns

class TestDoSWithUnexpectedRevert(unittest.TestCase):

    testFile = "DoSWithUnexpectedRevert"
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
        
    def test_selfDestruct(self):
        parseAST = ParseAST()
        astFD = open(self.testPath+".ast","r")
        parseResults = parseAST.parse(astFD)
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        mapASTSourceToLineNumbers.analyser(self.testDir+"Contracts/"+self.testFile+".sol")
        analyseDoSPatterns = AnalyseDoSPatterns()
        analyseDoSPatterns.analyser()
        self.assertEqual(len(analyseDoSPatterns.statsDoSWithUnexpectedRevert), 1)
        self.assertEqual(analyseDoSPatterns.statsDoSWithUnexpectedRevert[0]["line"], "9")
        self.assertEqual(analyseDoSPatterns.statsDoSWithUnexpectedRevert[0]["info"], "send")
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
