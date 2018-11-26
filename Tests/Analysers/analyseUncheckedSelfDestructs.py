import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from Analysers.analyseUncheckedSelfDestructs import AnalyseUncheckedSelfDestructs

class TestUncheckedSelfDestructs(unittest.TestCase):

    testFile = "uncheckedSelfDestructs"
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
        analyseUncheckedSelfDestructs = AnalyseUncheckedSelfDestructs()
        analyseUncheckedSelfDestructs.analyser()
        self.assertEqual(len(analyseUncheckedSelfDestructs.statsConditionalCheckedSelfDestructs), 1)
        self.assertEqual(analyseUncheckedSelfDestructs.statsConditionalCheckedSelfDestructs[0]["line"], "13")
        self.assertEqual(len(analyseUncheckedSelfDestructs.statsUncheckedSelfDestructs), 1)
        self.assertEqual(analyseUncheckedSelfDestructs.statsUncheckedSelfDestructs[0]["line"], "17")
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
