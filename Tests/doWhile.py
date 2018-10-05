import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST

class TestDoWhileAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/doWhile.ast","w")
        errFD = open("./tests/doWhile.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/doWhile.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests.doWhile.ast','./tests/doWhile.err'])
        p.wait()
        
    def test_doWhile(self):
        parseAST = ParseAST()
        astFD = open("./tests/doWhile.ast","r")
        parseResults = parseAST.parse(astFD)
        self.assertEqual(parseResults['Counts']['DoWhileCount'], 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
