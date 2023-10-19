import unittest
from pattern_matching.glob_charset import Charset
from pattern_matching.glob_lit import Lit

class TestLitClass(unittest.TestCase):
    def test_match_one_char(self):
        vowels = Charset("aeiou")
        self.assertTrue(vowels.match("a"))
        self.assertTrue(vowels.match("e"))
        self.assertFalse(vowels.match("b"))

    def test_match_with_lit(self):
        matcher = Lit("a", Charset("bx", Charset("cz")))
        self.assertTrue(matcher.match("abc"))
        self.assertTrue(matcher.match("abz"))
        self.assertTrue(matcher.match("axc"))
        self.assertTrue(matcher.match("axz"))
        self.assertFalse(matcher.match("aez"))

if __name__ == '__main__':
    unittest.main()
