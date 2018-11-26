import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.functionCall import AnalyseFunctionCall

class TestFunctionCallAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/functionCall.ast","w")
        errFD = open("./tests/functionCall.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/functionCall.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/functionCall.ast','./tests/functionCall.err'])
        p.wait()
        
    def test_functionCall(self):
        parseAST = ParseAST()
        astFD = open("./tests/functionCall.ast","r")
        parseResults = parseAST.parse(astFD)
        self.assertEqual(parseResults['Counts']['FunctionCallCount'], 1)
        functionCalls = AnalyseFunctionCall.getAllFunctionCalls()
        self.assertEqual(len(functionCalls), 1)
        self.assertEqual(functionCalls[0],"foo")
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
