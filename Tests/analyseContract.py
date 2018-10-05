import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.contract import AnalyseContract

class TestContractNames(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/multipleContracts.ast","w")
        errFD = open("./tests/multipleContracts.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/multipleContracts.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/multipleContracts.ast','./tests/multipleContracts.err'])
        p.wait()
        
    def test_contractName(self):
        parseAST = ParseAST()
        astFD = open("./tests/multipleContracts.ast","r")
        parseResults = parseAST.parse(astFD)
        contracts = AnalyseContract.getAllContractNames()
        for item in contracts:
            print("Contract Name: " + item)
        self.assertEqual(len(contracts), 2)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
