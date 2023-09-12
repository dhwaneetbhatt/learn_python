import unittest
from glob_not import Not
from glob_charset import Charset
from glob_lit import Lit

class TestLitClass(unittest.TestCase):
    def test_match_not_charset(self):
        matcher = Not(Charset("aeiou"))
        self.assertFalse(matcher.match("a"))
        self.assertFalse(matcher.match("e"))

    def test_match_not_lit(self):
        matcher = Not(Lit("abc"))
        self.assertFalse(matcher.match("abc"))

if __name__ == '__main__':
    unittest.main()
