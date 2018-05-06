# Acess to parent module
import sys
sys.path.insert(0, "..")
import unittest
import analysis


class AnalysisTest(unittest.TestCase):
    var_test = "Hello World!"

    def test_frequency(self):
        expected_res = {'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 1,
                'f': 0, 'g': 0, 'h': 1, 'i': 0, 'j': 0,
                'k': 0, 'l': 3, 'm': 0, 'n': 0, 'o': 2,
                'p': 0, 'q': 0, 'r': 1, 's': 0, 't': 0,
                'u': 0, 'v': 0, 'w': 1, 'x': 0, 'y': 0, 'z': 0}

        res = analysis.frequency(self.var_test)
        res_param_1 = analysis.frequency(self.var_test, maximum=True)

        self.assertEqual(res, expected_res)
        self.assertEqual(res_param_1, ('l', 3))

    def test_first_letters(self):
        expected_res = ["H", "W"]
        res = analysis.firstLetters(self.var_test)
        self.assertEqual(res, expected_res)

    def test_last_letters(self):
        expected_res = ["o", "!"]
        res = analysis.lastLetters(self.var_test)
        self.assertEqual(res, expected_res)


if __name__ == "__main__":
    unittest.main()
