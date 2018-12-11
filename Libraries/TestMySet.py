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

import subprocess, os, sys
from myset import MySet

class TestMySet():
    def test(self):
        _gen = MySet()
        _kill = MySet()
        _out = MySet()
        _in = MySet()
        _gen.add("a","node1")
        _diff = _gen.difference(_kill)
        print("Diff: " + str(_diff._set))
        _out = _in.union(_diff)
        print("Out: " + str(_out._set))
if __name__ == '__main__':
    t = TestMySet()
    t.test()
