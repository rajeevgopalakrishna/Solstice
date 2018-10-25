class MapASTSourceToLineNumbers:
    accumulatedCharacterCounts = []
    inputFile = ""
    
    def analyser(self, processFile):
        MapASTSourceToLineNumbers.inputFile = processFile        
        print("Runing MapASTSourceToLineNumbers on " + self.inputFile)
        inputFileFD = open(MapASTSourceToLineNumbers.inputFile,"r")
        lines = inputFileFD.readlines()
        for index in range(len(lines)):
            if (index != 0):
                self.accumulatedCharacterCounts.append(len(lines[index]) + self.accumulatedCharacterCounts[index-1])
            else:
                self.accumulatedCharacterCounts.append(len(lines[index]))
        inputFileFD.close()
        
    def getLine(self, characterIndex):
        for i, val in (enumerate(self.accumulatedCharacterCounts)):
            if (val > characterIndex):
                return (i+1)
        return(-1)
        
    def chkStringPresent(self, stringOfInterest, fromSrc, toSrc):
        fromChar = int(fromSrc.split(":",)[0]) + int(fromSrc.split(":",)[1])
        toChar = int(toSrc.split(":",)[0])
        inputFileFD = open(MapASTSourceToLineNumbers.inputFile,"r")
        inputFileFD.seek(fromChar)
        readString = inputFileFD.read(toChar-fromChar)
        if(readString.find(stringOfInterest) == -1):
            return False
        else:
            return True
    
    def chkStringPresentVariableVisibility(self, stringOfInterest, typeSrc, varSrc):
        fromChar = int(typeSrc.split(":",)[0]) + int(typeSrc.split(":",)[1])
        toChar = int(varSrc.split(":",)[0]) + int(varSrc.split(":",)[1])
        inputFileFD = open(MapASTSourceToLineNumbers.inputFile,"r")
        inputFileFD.seek(fromChar)
        readString = inputFileFD.read(toChar-fromChar)
        if(readString.find(stringOfInterest) == -1):
            return False
        else:
            return True
