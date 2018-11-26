import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from Analysers.analyseExternalContractInteractions import AnalyseExternalContractInteractions

class TestExternalContractInteractions(unittest.TestCase):

    testFile = "externalContractInteractions"
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
        analyseExternalContractInteractions = AnalyseExternalContractInteractions()
        analyseExternalContractInteractions.analyser()
        self.assertEqual(len(analyseExternalContractInteractions.statsTransfers), 1)
        self.assertEqual(analyseExternalContractInteractions.statsTransfers[0]["line"], "6")
        self.assertEqual(len(analyseExternalContractInteractions.statsSends), 1)
        self.assertEqual(analyseExternalContractInteractions.statsSends[0]["line"], "7")
        self.assertEqual(len(analyseExternalContractInteractions.statsCalls), 1)
        self.assertEqual(analyseExternalContractInteractions.statsCalls[0]["line"], "8")
        self.assertEqual(len(analyseExternalContractInteractions.statsDelegateCalls), 1)
        self.assertEqual(analyseExternalContractInteractions.statsDelegateCalls[0]["line"], "9")
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
