#	Copyright (c) 2018 Rajeev Gopalakrishna
#
#	This file is part of Solstice.
#
#	Solstice is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	Solstice is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with Solstice.  If not, see <http://www.gnu.org/licenses/>.

class ContractDefinition:
    registry = []
    nodeType = "ContractDefinition"

    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.baseContracts = node.get("baseContracts")
        self.contractDependencies = node.get("contractDependencies")
        self.contractKind = node.get("contractKind")
        self.documentation = node.get("documentation")
        self.fullyImplemented = node.get("fullyImplemented")
        self.id = node.get("id")
        self.linearizedBaseContracts = node.get("linearizedBaseContracts")
        self.name = node.get("name")
        self.scope = node.get("scope")
        self.src = node.get("src")
        
