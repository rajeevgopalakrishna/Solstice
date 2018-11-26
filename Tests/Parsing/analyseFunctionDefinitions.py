import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.functionDefinition import AnalyseFunctionDefinition
class TestFunctionDefinitions(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/functionDefinition.ast","w")
        errFD = open("./tests/functionDefinition.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/functionDefinition.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/functionDefinitions.ast','./tests/functionDefinitions.err'])
        p.wait()
        
    def test_functionDefinition(self):
        parseAST = ParseAST()
        astFD = open("./tests/functionDefinition.ast","r")
        parseResults = parseAST.parse(astFD)
        functionDefinitions = AnalyseFunctionDefinition.getAllFunctionDefinitions()
        for item in functionDefinitions:
            print("Function Definition Name: " + item)
        self.assertEqual(len(functionDefinitions), 2)
        functionDefinitionsPublicVisibility = AnalyseFunctionDefinition.getAllFunctionDefinitionsWithPublicVisibility()
        for item in functionDefinitionsPublicVisibility:
            print("Public Function Definition Name: " + item)
        self.assertEqual(len(functionDefinitionsPublicVisibility), 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
