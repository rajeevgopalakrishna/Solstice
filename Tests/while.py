import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST

class TestWhileAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/while.ast","w")
        errFD = open("./tests/while.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/while.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests.while.ast','./tests/while.err'])
        p.wait()
        
    def test_while(self):
        parseAST = ParseAST()
        astFD = open("./tests/while.ast","r")
        parseResults = parseAST.parse(astFD)
        self.assertEqual(parseResults['Counts']['WhileCount'], 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
