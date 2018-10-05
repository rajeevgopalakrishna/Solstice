import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST

class TestEventAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/event.ast","w")
        errFD = open("./tests/event.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/event.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/event.ast','./tests/event.err'])
        p.wait()
        
    def test_event(self):
        parseAST = ParseAST()
        astFD = open("./tests/event.ast","r")
        parseResults = parseAST.parse(astFD)
        self.assertEqual(parseResults['Counts']['EventCount'], 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
