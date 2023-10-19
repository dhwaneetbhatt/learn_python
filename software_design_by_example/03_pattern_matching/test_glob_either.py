import unittest

from pattern_matching.glob_either import Either
from pattern_matching.glob_lit import Lit

class TestEitherMatcher(unittest.TestCase):
    def test_either_two_literals_first(self):
        self.assertTrue(Either([Lit("a"), Lit("b")]).match("a"))

    def test_either_two_literals_not_both(self):
        self.assertFalse(Either([Lit("a"), Lit("b")]).match("ab"))

    def test_either_followed_by_literal_match(self):
        matcher = Either([Lit("a"), Lit("b")], Lit("c"))
        self.assertTrue(matcher.match("ac"))
        self.assertTrue(matcher.match("bc"))

    def test_either_followed_by_literal_no_match(self):
        self.assertFalse(Either([Lit("a"), Lit("b")], Lit("c")).match("ax"))

    def test_either_matches_multiple_literals(self):
        matcher = Either([
            Lit("abc"),
            Lit("def"),
            Lit("xyz")
        ], Lit(" is my favorite triplet"))
        self.assertTrue(matcher.match("abc is my favorite triplet"))
        self.assertTrue(matcher.match("def is my favorite triplet"))
        self.assertTrue(matcher.match("xyz is my favorite triplet"))

if __name__ == '__main__':
    unittest.main()
