import unittest

from glob_either import Either
from glob_lit import Lit

class TestEitherMatcher(unittest.TestCase):
    def test_either_two_literals_first(self):
        self.assertTrue(Either(Lit("a"), Lit("b")).match("a"))

    def test_either_two_literals_not_both(self):
        self.assertFalse(Either(Lit("a"), Lit("b")).match("ab"))

    def test_either_followed_by_literal_match(self):
        self.assertTrue(Either(Lit("a"), Lit("b"), Lit("c")).match("ac"))

    def test_either_followed_by_literal_no_match(self):
        self.assertFalse(Either(Lit("a"), Lit("b"), Lit("c")).match("ax"))

if __name__ == '__main__':
    unittest.main()
