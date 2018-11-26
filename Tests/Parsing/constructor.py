import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST
from AnalyseAST.functionDefinition import AnalyseFunctionDefinition
class TestConstructor(unittest.TestCase):

    testFile = "functionConstructor"
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
        
    def test_functionConstructor(self):
        parseAST = ParseAST()
        astFD = open(self.testPath+".ast","r")
        parseResults = parseAST.parse(astFD)
        constructors = AnalyseFunctionDefinition.getAllConstructors()
        self.assertEqual(len(constructors), 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
