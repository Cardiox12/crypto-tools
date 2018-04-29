import sys
sys.path.insert(0, '..')
import substitute
import unittest


class SubstituteTest(unittest.TestCase):
	var_test = "Hello World!"
	def test_encode(self):
		res = substitute.encode(self.var_test, 4)

