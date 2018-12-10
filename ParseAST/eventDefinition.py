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

class EventDefinition:
    registry = []
    nodeType = "EventDefinition"


    def __init__(self, node):
        self.registry.append(self)
        self.parent = None
        self.children = []
        self.anonymous = node.get("anonymous'")
        self.documentation = node.get("documentation'")
        self.id = node.get("id'")
        self.name = node.get("name'")
        self.src = node.get("src'")
        
