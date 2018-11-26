import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.functionCall import AnalyseFunctionCall

class TestExceptionsAST(unittest.TestCase):

    testFile = "exceptions"
    testDir = "./Tests/Parsing/"
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
        self.assertEqual(parseResults['Counts']['FunctionCallCount'], 3)
        functionCallNames = AnalyseFunctionCall.getAllFunctionCallNames()
        self.assertEqual(len(functionCallNames), 3)
        self.assertIn("assert", functionCallNames)
        self.assertIn("require", functionCallNames)
        self.assertIn("revert", functionCallNames)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
