import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.functionDefinition import AnalyseFunctionDefinition
class TestConstructor(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/functionConstructor.ast","w")
        errFD = open("./tests/functionConstructor.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/functionConstructor.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/functionConstructor.ast','./tests/functionConstructor.err'])
        p.wait()
        
    def test_functionConstructor(self):
        parseAST = ParseAST()
        astFD = open("./tests/functionConstructor.ast","r")
        parseResults = parseAST.parse(astFD)
        constructors = AnalyseFunctionDefinition.getAllConstructors()
        self.assertEqual(len(constructors), 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
