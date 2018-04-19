# Acess to parent module
import sys
sys.path.insert(0, "..")
import unittest
from analysis import *


class AnalysisTest(unittest.TestCase):
    def test_frequency(self):
        dict = {'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 1,
                'f': 0, 'g': 0, 'h': 1, 'i': 0, 'j': 0,
                'k': 0, 'l': 3, 'm': 0, 'n': 0, 'o': 2,
                'p': 0, 'q': 0, 'r': 1, 's': 0, 't': 0,
                'u': 0, 'v': 0, 'w': 1, 'x': 0, 'y': 0, 'z': 0}
        res = frequency("Hello World!")
        res2 = frequency("Hello World!")
        print("assert 1")
        self.assertEqual(res, dict)
        print("assert 2")
        self.assertEqual(res2, dict)

if __name__ == "__main__":
    unittest.main()
