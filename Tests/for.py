import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST

class TestForAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/for.ast","w")
        errFD = open("./tests/for.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/for.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests.for.ast','./tests/for.err'])
        p.wait()
        
    def test_for(self):
        parseAST = ParseAST()
        astFD = open("./tests/for.ast","r")
        parseResults = parseAST.parse(astFD)
        self.assertEqual(parseResults['Counts']['ForCount'], 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
