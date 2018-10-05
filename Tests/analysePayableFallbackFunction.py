import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.functionDefinition import AnalyseFunctionDefinition
class TestFunctionPayableFallback(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/functionPayableFallback.ast","w")
        errFD = open("./tests/functionPayableFallback.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/functionPayableFallback.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/functionPayableFallback.ast','./tests/functionPayableFallback.err'])
        p.wait()
        
    def test_functionPayableFallback(self):
        parseAST = ParseAST()
        astFD = open("./tests/functionPayableFallback.ast","r")
        parseResults = parseAST.parse(astFD)
        payableFunctionFallbackCount = AnalyseFunctionDefinition.hasPayableFallbackFunction()
        self.assertEqual(payableFunctionFallbackCount, 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
