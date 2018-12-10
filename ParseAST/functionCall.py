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

class FunctionCall:
    registry = []
    nodeType = "FunctionCall"

    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.argumentTypes = node.get("argumentTypes")
        self.arguments = node.get("arguments")
        self.expression = node.get("expression")
        self.id = node.get("id")
        self.isConstant = node.get("isConstant")
        self.isLValue = node.get("isLValue")
        self.isPure = node.get("isPure")
        self.kind = node.get("kind")
        self.lValueRequested = node.get("lValueRequested")
        self.names = node.get("names")
        self.src = node.get("src")
        self.typeDescriptions = node.get("typeDescriptions")
        self.name = node.get("expression").get("name")
