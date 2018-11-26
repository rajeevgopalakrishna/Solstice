import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.functionCall import AnalyseFunctionCall

class TestFunctionCalls(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/functionCall.ast","w")
        errFD = open("./tests/functionCall.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/functionCall.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/functionCalls.ast','./tests/functionCalls.err'])
        p.wait()
        
    def test_contractName(self):
        parseAST = ParseAST()
        astFD = open("./tests/functionCall.ast","r")
        parseResults = parseAST.parse(astFD)
        functionCalls = AnalyseFunctionCall.getAllFunctionCalls()
        for item in functionCalls:
            print("Function Call Name: " + item)
        self.assertEqual(len(functionCalls), 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
