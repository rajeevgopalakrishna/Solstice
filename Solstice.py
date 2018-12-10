import subprocess, os, sys, getopt, logging
from ParseAST.parseAST import ParseAST
from Analysers.analyseExternalContractInteractions import AnalyseExternalContractInteractions
from Analysers.analyseDefaultVisibility import AnalyseDefaultVisibility
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers
from Analysers.analyseExceptions import AnalyseExceptions
from Analysers.analyseContractFeatures import AnalyseContractFeatures
from Analysers.analyseUncheckedCalls import AnalyseUncheckedCalls
from Analysers.analyseUncheckedSelfDestructs import AnalyseUncheckedSelfDestructs
from Analysers.analyseDoSPatterns import AnalyseDoSPatterns
from Analysers.analyseDeprecatedConstructs import AnalyseDeprecatedConstructs
from Analysers.analyseDefsUses import AnalyseDefsUses
from Analysers.analyseReentrancy import AnalyseReentrancy
from Analysers.analyseControlFlowGraph import AnalyseControlFlowGraph
from Analysers.analyseTaintedVariables import AnalyseTaintedVariables
from Analysers.analyseUninitialisedStoragePointers import AnalyseUninitialisedStoragePointers

class Solstice:
    inputFile = ""
    outputFile = ""
    astFile = ""
    errFile = ""
    loggingLevel = "INFO"
    runAllAnalysers = True
    runAnalyser1 = False
    runAnalyser2 = False
    runAnalyser3 = False
    runAnalyser4 = False
    runAnalyser5 = False
    runAnalyser6 = False
    runAnalyser7 = False
    runAnalyser8 = False
    runAnalyser9 = False
    runAnalyser10 = False
    runAnalyser11 = False
    runAnalyser12 = False
    runAnalyser13 = False
    runAnalyser14 = False
    runAnalyser15 = False

    def main(self, argv):
        try:
            opts, args = getopt.getopt(argv,"hdi:o:",["help","ifile=","ofile=","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"])
        except getopt.GetoptError:
            print("python3 Solstice.py -i <Input Solidity File> [-o <Output Report File>] [--<AnalyserID to be run>, ..]")
            print("Example: python3 Solstice.py -i ./Tests/Analysers/Contracts/Real-World/GnosisSafe.sol --1 --2")
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print("python3 Solstice.py -i <Input Solidity File> [-o <Output Report File>] [--<AnalyserID to be run>, ..]")
                print("Example: python3 Solstice.py -i ./Tests/Analysers/Contracts/Real-World/GnosisSafe.sol --1 --2")
                sys.exit()
            elif opt == "-d":
                print("Setting Logging level to debug")
                self.loggingLevel = "DEBUG"
                AnalyseDefsUses.logginglevel = "DEBUG"
                logging.basicConfig(level=self.loggingLevel)
            elif opt in ("-i", "--ifile"):
                self.inputFile = arg
                logging.debug("Input file is ", self.inputFile)
            elif opt in ("-o", "--ofile"):
                self.outputFile = arg
                print("Output file is ", self.outputFile)
            elif opt in ("--1"):
                self.runAllAnalysers = False
                self.runAnalyser1 = True
            elif opt in ("--2"):
                self.runAllAnalysers = False
                self.runAnalyser2 = True
            elif opt in ("--3"):
                self.runAllAnalysers = False
                self.runAnalyser3 = True
            elif opt in ("--4"):
                self.runAllAnalysers = False
                self.runAnalyser4 = True
            elif opt in ("--5"):
                self.runAllAnalysers = False
                self.runAnalyser5 = True
            elif opt in "--6":
                self.runAllAnalysers = False
                self.runAnalyser6 = True
            elif opt in ("--7"):
                self.runAllAnalysers = False
                self.runAnalyser7 = True
            elif opt in ("--8"):
                self.runAllAnalysers = False
                self.runAnalyser8 = True
            elif opt in ("--9"):
                self.runAllAnalysers = False
                self.runAnalyser9 = True
            elif opt in ("--10"):
                self.runAllAnalysers = False
                self.runAnalyser10 = True
            elif opt in ("--11"):
                self.runAllAnalysers = False
                self.runAnalyser11 = True
            elif opt in ("--12"):
                self.runAllAnalysers = False
                self.runAnalyser12 = True
            elif opt in ("--13"):
                self.runAllAnalysers = False
                self.runAnalyser13 = True
            elif opt in ("--14"):
                self.runAllAnalysers = False
                self.runAnalyser14 = True
            elif opt in ("--15"):
                self.runAllAnalysers = False
                self.runAnalyser15 = True

        if (self.inputFile == ""):
            print("Usage:")
            print("  python3 Solstice.py -i <Input Solidity File> [-o <Output Report File>] [--<AnalyserID to be run>, ..]")
            print("Example:")
            print("  python3 Solstice.py -i ./Tests/Analysers/Contracts/Real-World/GnosisSafe.sol --1 --2")
            exit()
                

    def process(self):
        self.astFile = self.inputFile + ".ast"
        self.errFile = self.inputFile + ".err"
        astFD = open(self.astFile,"w")
        errFD = open(self.errFile,"w")
        p = subprocess.Popen(['solc','--ast-compact-json',self.inputFile], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def analyse(self):
        parseAST = ParseAST()
        astFD = open(self.astFile,"r")
        parseResults = parseAST.parse(astFD)
        
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        mapASTSourceToLineNumbers.analyser(self.inputFile)

        if (self.runAllAnalysers or self.runAnalyser1):
            analyseContractFeatures = AnalyseContractFeatures()
            analyseContractFeatures.analyser()
            
        if (self.runAllAnalysers or self.runAnalyser2):
            analyseControlFlowGraph = AnalyseControlFlowGraph()
            analyseControlFlowGraph.analyser()

        if (self.runAllAnalysers or self.runAnalyser3):
            analyseDefaultVisibility = AnalyseDefaultVisibility()
            analyseDefaultVisibility.analyser()

        if (self.runAllAnalysers or self.runAnalyser4):
            analyseDeprecatedConstructs = AnalyseDeprecatedConstructs()
            analyseDeprecatedConstructs.analyser()

        if (self.runAllAnalysers or (self.runAnalyser5 or self.runAnalyser6 or self.runAnalyser7)):
            analyseDoSPatterns = AnalyseDoSPatterns()
            analyseDoSPatterns.analyser()

        if (self.runAllAnalysers or self.runAnalyser8):
            analyseExternalContractInteractions = AnalyseExternalContractInteractions()
            analyseExternalContractInteractions.analyser()

        if (self.runAllAnalysers or self.runAnalyser9):
            analyseExceptions = AnalyseExceptions()
            analyseExceptions.analyser()

        if (self.runAllAnalysers or self.runAnalyser10):
            analyseReentrancy = AnalyseReentrancy()
            analyseReentrancy.analyser()

        if (self.runAllAnalysers or self.runAnalyser11):
            analyseUncheckedCalls = AnalyseUncheckedCalls()
            analyseUncheckedCalls.analyser()

        if (self.runAllAnalysers or self.runAnalyser12):
            analyseUncheckedSelfDestructs = AnalyseUncheckedSelfDestructs()
            analyseUncheckedSelfDestructs.analyser()

        if (self.runAllAnalysers or self.runAnalyser13):
            analyseUninitialisedStoragePointers = AnalyseUninitialisedStoragePointers()
            analyseUninitialisedStoragePointers.analyser()

        if (self.runAllAnalysers or self.runAnalyser14):
            analyseDefsUses = AnalyseDefsUses()
            analyseDefsUses.analyser()

        if (self.runAllAnalysers or self.runAnalyser15):
            analyseTaintVariables = AnalyseTaintedVariables()
            analyseTaintVariables.analyser()

        astFD.close()
        
if __name__ == "__main__":
    solstice = Solstice()
    solstice.main(sys.argv[1:])
    solstice.process()
    solstice.analyse()
   

