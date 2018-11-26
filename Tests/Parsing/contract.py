import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.contract import AnalyseContract

class TestContractNames(unittest.TestCase):

    testFile = "multipleContracts"
    testDir = "./Tests/Parsing/"
    testPath = testDir+testFile

    def setUp(self):
        astFD = open(self.testPath+".ast","w")
        errFD = open(self.testPath+".err","w")
        p = subprocess.Popen(['solc','--ast-compact-json',self.testDir+'/Contracts/'+self.testFile+'.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f',self.testPath+'.ast',self.testPath+'.err'])
        p.wait()
        
    def test_contractName(self):
        parseAST = ParseAST()
        astFD = open(self.testPath+".ast","r")
        parseResults = parseAST.parse(astFD)
        contracts = AnalyseContract.getAllContractNames()
        for item in contracts:
            print("Contract Name: " + item)
        self.assertEqual(len(contracts), 2)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
