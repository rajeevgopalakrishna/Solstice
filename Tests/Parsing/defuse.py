import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from ParseAST.contractDefinition import ContractDefinition
from AnalyseAST.defUse import DefUseAnalysis


class TestDefUseAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/defuse.ast","w")
        errFD = open("./tests/defuse.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/defuse.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

#    def tearDown(self):
#        p = subprocess.Popen(['rm','-f','./tests/defuse.ast','./tests/defuse.err'])
#        p.wait()
        
    def test_defuse(self):
        parseAST = ParseAST()
        astFD = open("./tests/defuse.ast","r")
        parseResults = parseAST.parse(astFD)
        defs = DefUseAnalysis.getAllDefs()
        for _def in defs:
            print("Def: " + _def)
        uses = DefUseAnalysis.getAllUses()
        for _use in uses:
            print("Use: " + _use)

        
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
