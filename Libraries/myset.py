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

class MySet:
    def __init__(self):
        self._set = set()
        self.idToNodeMapping = {}

    def add(self, id, node):
        if(self._set is not None):
            self._set.add(id)
            self.idToNodeMapping[id] = node

    def union(self, mySet):
        retSet = MySet()
        retSet._set = self._set
        retSet.idToNodeMapping = self.idToNodeMapping.copy()
        
        if (mySet is not None):
            retSet._set = retSet._set.union(mySet._set)
            for id in mySet.idToNodeMapping:
                retSet.idToNodeMapping[id] = mySet.idToNodeMapping[id]
        return retSet
    
    def difference(self, mySet):
        if(self is not None):
            retSet = MySet()
            retSet._set = self._set
            retSet.idToNodeMapping = self.idToNodeMapping.copy()
            
            retSet._set = retSet._set.difference(mySet._set)
            for id in mySet.idToNodeMapping:
                if (id in retSet.idToNodeMapping):
                    del retSet.idToNodeMapping[id]
        return retSet
        
    def print(self):
        print(str(_set))
