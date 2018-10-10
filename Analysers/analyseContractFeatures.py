from AnalyseAST.contract import AnalyseContract
from AnalyseAST.functionDefinition import AnalyseFunctionDefinition
from AnalyseAST.variable import AnalyseVariable
from AnalyseAST.expression import AnalyseExpression
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers

class AnalyseContractFeatures:

    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Contract Features >>>>>>>>>>")
        
        contracts = AnalyseContract.getAllContracts()
        for contract in contracts:
            print("\n********** Contract Features **********")
            print("Contract definition: " + contract.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(contract.src.split(":",)[0]))))
        
        functionDefinitions = AnalyseFunctionDefinition.getAllFunctionDefinitions()
        for function in functionDefinitions:
            print("\n********** Function Features **********")
            print("Function definition: " + function.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(function.src.split(":",)[0]))))
            if (function.isConstructor):
                print("Constructor")
            print("Visibility: " + function.visibility)
            print("State Mutability: " + function.stateMutability)
            if (AnalyseFunctionDefinition.isFallbackFunction(function)):
                print("Fallback function")
            if (AnalyseFunctionDefinition.isPayableFallbackFunction(function)):
                print("Payable Fallback function")
            modifiers = function.modifiers
            for modifier in modifiers:
                print("Modifier: " + modifier['modifierName']['name'])
                    
        variableDeclarations = AnalyseVariable.getAllVariables()
        for variable in variableDeclarations:
            print("\n********** Variable Features **********")
            print("Variable declaration: " + variable.name  + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(variable.src.split(":",)[0]))))
            if (variable.stateVariable):
                print("State variable")
            else:
                print("Local variable")
