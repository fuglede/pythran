from pythran import cxx_generator, compile
from imp import load_dynamic
import unittest
import os

class TestEnv(unittest.TestCase):

    def run_test(self, code, *params, **interface):
        for name in sorted(interface.keys()):
            modname="test_"+name
            print modname
            mod = cxx_generator(modname, code, interface)
            pymod = load_dynamic(modname,compile(os.environ.get("CXX","c++"),mod))
            res = getattr(pymod,name)(*params)
            #print res

