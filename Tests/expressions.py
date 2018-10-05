import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST

class TestExpressionsAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/expressions.ast","w")
        errFD = open("./tests/expressions.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/expressions.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/expressions.ast','./tests/expressions.err'])
        p.wait()
        
    def test_expressions(self):
        parseAST = ParseAST()
        astFD = open("./tests/expressions.ast","r")
        parseResults = parseAST.parse(astFD)
        self.assertEqual(parseResults['Counts']['ExpressionCount'], 30)
        self.assertEqual(parseResults['AST'].children[0].name, "TestExpressions")
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
