import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST

class TestIfThenElseAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/ifThenElse.ast","w")
        errFD = open("./tests/ifThenElse.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/ifThenElse.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests.ifThenElse.ast','./tests/ifThenElse.err'])
        p.wait()
        
    def test_ifThenElse(self):
        parseAST = ParseAST()
        astFD = open("./tests/ifThenElse.ast","r")
        parseResults = parseAST.parse(astFD)
        self.assertEqual(parseResults['Counts']['ifCondition'], 1)
        self.assertEqual(parseResults['Counts']['ifTrueBody'], 1)
        self.assertEqual(parseResults['Counts']['ifFalseBody'], 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
