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
