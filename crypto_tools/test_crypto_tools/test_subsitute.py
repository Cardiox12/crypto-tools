import sys
sys.path.insert(0, '..')
import substitute
import unittest
import string


class SubstituteTest(unittest.TestCase):
	var_test = string.ascii_lowercase
	expected_res = 'fghijklmnopqrstuvwxyzabcde'

	def test_encode(self):
		res = substitute.encode(self.var_test, 5)

		self.assertEqual(res, self.expected_res)

	def test_decode(self):
		res = substitute.decode(self.expected_res, 5)

		self.assertEqual(res, string.ascii_lowercase)

	def test_decode_simple(self):
		res = substitute.decode_simple(self.var_test, 5)
		expected_res_decode_simple = "\]^_`abcdefghijklmnopqrstu"

		self.assertEqual(res, expected_res_decode_simple)

	def test_bruteforce(self):
		res = substitute.brute_force(self.var_test)

		self.assertIn(self.expected_res, res)

	def test_bruteforce_simple(self):
		res = substitute.brute_force_simple(self.var_test)
		expected_res_in = """STUVWXYZ[\\]^_`abcdefghijkl"""

		self.assertIn(expected_res_in, res)


