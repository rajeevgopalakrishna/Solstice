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

from ParseAST.variableDeclaration import VariableDeclaration

class AnalyseVariable:
    def getAllVariables():
        return VariableDeclaration.registry

    def getAllStateVariables():
        stateVariables = []
        for variable in VariableDeclaration.registry:
            if (variable.stateVariable):
                stateVariables.append(variable)
        return stateVariables

    def getAllStorageVariables():
        storageVariables = []
        for variable in VariableDeclaration.registry:
            if (variable.storageLocation == "storage"):
                storageVariable.append(variable)
        return storageVariables

    def getAllMemoryVariables():
        memoryVariables = []
        for variable in VariableDeclaration.registry:
            if (variable.storageLocation == "memory"):
                memoryVariable.append(variable)
        return memoryVariables

    def getVariableNameForId(id):
        for variable in VariableDeclaration.registry:
            if (variable.id == id):
                return variable.name
        return "Error"
        
                
        
    

    
    
    
