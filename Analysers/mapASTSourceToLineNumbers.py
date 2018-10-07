class MapASTSourceToLineNumbers:
    accumulatedCharacterCounts = []

    def analyser(self, inputFile):
        print("Runing MapASTSourceToLineNumbers....")
        inputFileFD = open(inputFile,"r")
        lines = inputFileFD.readlines()
        for index in range(len(lines)):
            if (index != 0):
                self.accumulatedCharacterCounts.append(len(lines[index]) + self.accumulatedCharacterCounts[index-1])
            else:
                self.accumulatedCharacterCounts.append(len(lines[index]))
            
    def getLine(self, characterIndex):
        for i, val in (enumerate(self.accumulatedCharacterCounts)):
            if (val > characterIndex):
                return (i+1)
        return(-1)
        
