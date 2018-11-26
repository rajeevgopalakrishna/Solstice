import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.identifier import AnalyseIdentifier
from AnalyseAST.variable import AnalyseVariable

class TestIdentifiersAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/identifiers.ast","w")
        errFD = open("./tests/identifiers.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/identifiers.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

#    def tearDown(self):
#        p = subprocess.Popen(['rm','-f','./tests/identifiers.ast','./tests/identifiers.err'])
#        p.wait()
        
    def test_identifiers(self):
        parseAST = ParseAST()
        astFD = open("./tests/identifiers.ast","r")
        parseResults = parseAST.parse(astFD)
        identifiers = AnalyseIdentifier.getAllIdentifiers()
        for identifier in identifiers:
            print("Identifier In Expression: " + identifier.name)

        

        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
