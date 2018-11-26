import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.functionDefinition import AnalyseFunctionDefinition
class TestFunctionFallbacks(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/functionFallback.ast","w")
        errFD = open("./tests/functionFallback.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/functionFallback.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/functionFallback.ast','./tests/functionFallback.err'])
        p.wait()
        
    def test_functionFallback(self):
        parseAST = ParseAST()
        astFD = open("./tests/functionFallback.ast","r")
        parseResults = parseAST.parse(astFD)
        functionFallbackCount = AnalyseFunctionDefinition.hasFallbackFunction()
        payableFunctionFallbackCount = AnalyseFunctionDefinition.hasPayableFallbackFunction()
        self.assertEqual(functionFallbackCount, 1)
        self.assertEqual(payableFunctionFallbackCount, 0)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
