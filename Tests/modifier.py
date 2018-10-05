import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST

class TestModifierAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/modifier.ast","w")
        errFD = open("./tests/modifier.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/modifier.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/modifier.ast','./tests/modifier.err'])
        p.wait()
        
    def test_modifier(self):
        parseAST = ParseAST()
        astFD = open("./tests/modifier.ast","r")
        parseResults = parseAST.parse(astFD)
        self.assertEqual(parseResults['Counts']['ModifierCount'], 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
