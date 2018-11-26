import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST

class TestForAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./Tests/Parsing/for.ast","w")
        errFD = open("./Tests/Parsing/for.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./Tests/Parsing/for.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./Tests/Parsing/for.ast','./Tests/Parsing/for.err'])
        p.wait()
        
    def test_for(self):
        parseAST = ParseAST()
        astFD = open("./Tests/Parsing/for.ast","r")
        parseResults = parseAST.parse(astFD)
        self.assertEqual(parseResults['Counts']['ForCount'], 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
