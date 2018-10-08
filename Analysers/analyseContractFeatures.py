from AnalyseAST.contract import AnalyseContract
from AnalyseAST.functionDefinition import AnalyseFunctionDefinition
from AnalyseAST.variable import AnalyseVariable
from AnalyseAST.expression import AnalyseExpression
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers

class AnalyseContractFeatures:

    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n!!!!!!!!!! Analyser: Contract Features !!!!!!!!!!")
        
        print("********** Contract Features **********")
        contracts = AnalyseContract.getAllContracts()
        for contract in contracts:
            print("Contract definition: " + contract.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(contract.src.split(":",)[0]))))
            print("########################################")
        
        functionDefinitions = AnalyseFunctionDefinition.getAllFunctionDefinitions()
        for function in functionDefinitions:
            print("********** Function Features **********")
            print("Function definition: " + function.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(function.src.split(":",)[0]))))
            if (function.isConstructor):
                print("Constructor")
            print("Visibility: " + function.visibility)
            print("State Mutability: " + function.stateMutability)
            if (AnalyseFunctionDefinition.isFallbackFunction(function)):
                print("Fallback function")
            if (AnalyseFunctionDefinition.isPayableFallbackFunction(function)):
                print("Payable Fallback function")
            print("########################################")
            
        
        variableDeclarations = AnalyseVariable.getAllVariables()
        for variable in variableDeclarations:
            print("********** Variable Features **********")
            print("Variable declaration: " + variable.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(variable.src.split(":",)[0]))))
            if (variable.stateVariable):
                print("State variable")
            else:
                print("Local variable")
