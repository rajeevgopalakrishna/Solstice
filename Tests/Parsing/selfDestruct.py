import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.functionCall import AnalyseFunctionCall

class TestSelfDestructAST(unittest.TestCase):

    testFile = "selfDestruct"
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
        
    def test_selfDestruct(self):
        parseAST = ParseAST()
        astFD = open(self.testPath+".ast","r")
        parseResults = parseAST.parse(astFD)
        self.assertEqual(parseResults['Counts']['FunctionCallCount'], 2)
        functionCalls = AnalyseFunctionCall.getAllFunctionCallNames()
        self.assertEqual(len(functionCalls), 2)
        self.assertEqual(functionCalls[0],"selfdestruct")
        self.assertEqual(functionCalls[1],"selfdestruct")
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
