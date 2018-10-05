import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.functionCall import AnalyseFunctionCall

class TestSelfDestructAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/selfDestruct.ast","w")
        errFD = open("./tests/selfDestruct.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/selfDestruct.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/selfDestruct.ast','./tests/selfDestruct.err'])
        p.wait()
        
    def test_selfDestruct(self):
        parseAST = ParseAST()
        astFD = open("./tests/selfDestruct.ast","r")
        parseResults = parseAST.parse(astFD)
        self.assertEqual(parseResults['Counts']['FunctionCallCount'], 1)
        functionCalls = AnalyseFunctionCall.getAllFunctionCalls()
        self.assertEqual(len(functionCalls), 1)
        self.assertEqual(functionCalls[0],"selfdestruct")
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
