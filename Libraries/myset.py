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
