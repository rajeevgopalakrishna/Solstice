#    Copyright (C) 2018 Rajeev Gopalakrishna
#
#    This file is part of Solstice.
#
#    Solstice is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    Solstice is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
        

