import logging
from AnalyseAST.variable import AnalyseVariable
from Analysers.mapASTSourceToLineNumbers import MapASTSourceToLineNumbers

class AnalyseUninitialisedStoragePointers:
    statsUninitialisedStoragePointers = []
    
    def analyser(self):
        mapASTSourceToLineNumbers = MapASTSourceToLineNumbers()
        print("\n<<<<<<<<<< Analyser: Uninitialised Storage Variables >>>>>>>>>>")

        variables = AnalyseVariable.getAllVariables()
        
        for variable in variables:
            logging.debug("Variable: " + str(variable))
            logging.debug("stateVariable: " + str(variable.stateVariable))
            logging.debug("storageLocation: " + variable.storageLocation)
            logging.debug("type: " + variable.typeDescriptions.get("typeIdentifier"))
            isVariableUninitialised = True
            parent = variable.parent
            if ((parent.nodeType == "VariableDeclarationStatement" and parent.initialValue != None) or parent.nodeType == "FunctionDefinition"):
                isVariableUninitialised = False
            if (variable.stateVariable is False and
                isVariableUninitialised and
                (variable.storageLocation == "storage" or
                 (variable.storageLocation == "default" and
                   ("struct" in variable.typeDescriptions.get("typeIdentifier") or
                    "array" in variable.typeDescriptions.get("typeIdentifier") or
                    "mapping" in variable.typeDescriptions.get("typeIdentifier")
                   )
                 )
                )
            ):
                self.statsUninitialisedStoragePointers.append({
                    "line":str(mapASTSourceToLineNumbers.getLine(int(variable.src.split(":",)[0]))),
                    "info":"uninitialised storage pointer"
                })
                print("Uninitialised storage pointer " + variable.name + " at line:" + str(mapASTSourceToLineNumbers.getLine(int(variable.src.split(":",)[0]))))
        

