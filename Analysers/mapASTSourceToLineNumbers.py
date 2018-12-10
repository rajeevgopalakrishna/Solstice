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

import logging

class MapASTSourceToLineNumbers:
    accumulatedCharacterCounts = []
    inputFile = ""
    
    def analyser(self, processFile):
        MapASTSourceToLineNumbers.inputFile = processFile        
        logging.debug("Running MapASTSourceToLineNumbers on " + self.inputFile)
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
            inputFileFD.close()
            return False
        else:
            inputFileFD.close()
            return True
    
    def chkStringPresentVariableVisibility(self, stringOfInterest, typeSrc, varSrc):
        fromChar = int(typeSrc.split(":",)[0]) + int(typeSrc.split(":",)[1])
        toChar = int(varSrc.split(":",)[0]) + int(varSrc.split(":",)[1])
        inputFileFD = open(MapASTSourceToLineNumbers.inputFile,"r")
        inputFileFD.seek(fromChar)
        readString = inputFileFD.read(toChar-fromChar)
        if(readString.find(stringOfInterest) == -1):
            inputFileFD.close()
            return False
        else:
            inputFileFD.close()
            return True
