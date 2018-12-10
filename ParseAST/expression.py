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

class Expression:
    registry = []

    def __init__(self, node, typeOfExpression):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.nodeType = node.get("nodeType")
        self.argumentTypes = node.get("argumentTypes")
        self.arguments = node.get("arguments")
        self.id = node.get("id")
        self.isConstant = node.get("isConstant")
        self.isLValue = node.get("isLValue")
        self.isPure = node.get("isPure")
        self.lValueRequested = node.get("lValueRequested")
        self.operator = node.get("operator")
        self.prefix = node.get("prefix")
        self.src = node.get("src")
        self.subExpression = node.get("subExpression")
        self.typeDescriptions = node.get("typeDescriptions")
        self.leftHandSide = node.get("leftHandSide")
        self.rightHandSide = node.get("rightHandSide")
        self.leftExpression = node.get("leftExpression")
        self.rightExpression = node.get("rightExpression")
        self.overloadedDeclarations = node.get("overloadedDeclarations")
        self.referencedDeclaration = node.get("referencedDeclaration")
        self.name = node.get("name")
        self.commonType = node.get("commonType")
        self.components = node.get("components")
        self.hexValue = node.get("hexValue")
        self.kind = node.get("kind")
        self.subdenomination = node.get("subdenomination")
        self.value = node.get("value")
        self.isInlineArray = node.get("isInlineArray")
        self.memberName = node.get("memberName")
        self.type = typeOfExpression
