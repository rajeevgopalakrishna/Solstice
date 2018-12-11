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

class FunctionDefinition:
    registry = []
    nodeType = "FunctionDefinition"

    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.documentation = node.get("documentation")
        self.id = node.get("id")
        self.implemented = node.get("implemented")
        self.isConstructor = node.get("isConstructor")
        self.isDeclaredConst = node.get("isDeclaredConst")
        self.modifiers = node.get("modifiers")
        self.name = node.get("name")
        self.parameters = node.get("parameters")
        self.payable = node.get("payable")
        self.returnParameters = node.get("returnParameters")
        self.scope = node.get("scope")
        self.src = node.get("src")
        self.stateMutability = node.get("stateMutability")
        self.superFunction = node.get("superFunction")
        self.visibility = node.get("visibility")
        
        
