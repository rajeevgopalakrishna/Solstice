import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST

class TestStateVariableAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/stateVariable.ast","w")
        errFD = open("./tests/stateVariable.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/stateVariable.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/stateVariable.ast','./tests/stateVariable.err'])
        p.wait()
        
    def test_stateVariable(self):
        parseAST = ParseAST()
        astFD = open("./tests/stateVariable.ast","r")
        parseResults = parseAST.parse(astFD)
        self.assertEqual(parseResults['Counts']['VariableDeclarationCount'], 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
