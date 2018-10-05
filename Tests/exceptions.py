import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.functionCall import AnalyseFunctionCall

class TestExceptionsAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/exceptions.ast","w")
        errFD = open("./tests/exceptions.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/exceptions.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/exceptions.ast','./tests/exceptions.err'])
        p.wait()
        
    def test_exceptions(self):
        parseAST = ParseAST()
        astFD = open("./tests/exceptions.ast","r")
        parseResults = parseAST.parse(astFD)
        self.assertEqual(parseResults['Counts']['FunctionCallCount'], 3)
        functionCalls = AnalyseFunctionCall.getAllFunctionCalls()
        self.assertEqual(len(functionCalls), 3)
        self.assertIn("assert", functionCalls)
        self.assertIn("require", functionCalls)
        self.assertIn("revert", functionCalls)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
