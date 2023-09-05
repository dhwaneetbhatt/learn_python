import unittest
from glob_lit import Lit
from glob_any import Any

class TestAnyMatcher(unittest.TestCase):
    def test_match_empty_any(self):
        self.assertTrue(Any().match("abcdef"))

    def test_match_empty_string(self):
        self.assertTrue(Any().match(""))

    def test_match_as_prefix(self):
        self.assertTrue(Any(Lit("def")).match("abcdef"))

    def test_match_as_suffix(self):
        self.assertTrue(Lit("abc", Any()).match("abcdef"))

    def test_match_interior(self):
        self.assertTrue(Lit("a", Any(Lit("c"))).match("abc"))

if __name__ == '__main__':
    unittest.main()
