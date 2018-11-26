import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from Analysers.analyseContractFeatures import AnalyseContractFeatures

class TestContractFeatures(unittest.TestCase):

    testFile = "contractFeatures"
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
        analyseContractFeatures = AnalyseContractFeatures()
        analyseContractFeatures.analyser()
        self.assertEqual(len(analyseContractFeatures.statsContractDefinitions), 2)
        self.assertEqual(analyseContractFeatures.statsContractDefinitions[0]["line"], "3")
        self.assertEqual(len(analyseContractFeatures.statsFunctionDefinitions), 6)
        self.assertEqual(len(analyseContractFeatures.statsConstructors), 2)
        self.assertEqual(len(analyseContractFeatures.statsFallbackFunctions), 1)
        self.assertEqual(len(analyseContractFeatures.statsVariableDeclarations), 8)
        self.assertEqual(len(analyseContractFeatures.statsStateVariables), 5)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
