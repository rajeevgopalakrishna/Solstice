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

class VariableDeclaration:
    registry = []
    nodeType = "VariableDeclaration"

    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.constant = node["constant"]
        self.id = node.get("id")
        self.name = node.get("name")
        self.scope = node.get("scope")
        self.src = node.get("src")
        self.stateVariable = node.get("stateVariable")
        self.storageLocation = node.get("storageLocation")
        self.typeDescriptions = node.get("typeDescriptions")
        self.typeName = node.get("typeName")
        self.value = node.get("value")
        self.visibility =  node.get("visibility")
        
