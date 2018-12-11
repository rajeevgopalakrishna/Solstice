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

class Identifier:
    registry = []

    def __init__(self, node, type):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.argumentTypes = node.get("argumentTypes")
        self.id = node.get("id")
        self.name = node.get("name")
        self.nodeType = node.get("nodeType")        
        self.overloadedDeclarations = node.get("overloadedDeclarations")
        self.referencedDeclaration = node.get("referencedDeclaration")
        self.typeIdentifier = node.get("typeDescriptions").get("typeIdentifier")
        self.type = type
