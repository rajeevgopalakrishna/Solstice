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

import unittest
import subprocess, os, sys
from ParseAST.parseAST import ParseAST

class TestEventAST(unittest.TestCase):

    def setUp(self):
        astFD = open("./tests/event.ast","w")
        errFD = open("./tests/event.err","w")
        p = subprocess.Popen(['solc','--ast-compact-json','./tests/event.sol'], stdout=astFD,stderr=errFD)
        p.wait()
        astFD.close()
        errFD.close()

    def tearDown(self):
        p = subprocess.Popen(['rm','-f','./tests/event.ast','./tests/event.err'])
        p.wait()
        
    def test_event(self):
        parseAST = ParseAST()
        astFD = open("./tests/event.ast","r")
        parseResults = parseAST.parse(astFD)
        self.assertEqual(parseResults['Counts']['EventCount'], 1)
        astFD.close()
        
if __name__ == '__main__':
    unittest.main()
