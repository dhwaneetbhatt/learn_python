import unittest
from glob_lit import Lit

class TestLitClass(unittest.TestCase):
    def test_match_exact(self):
        self.assertTrue(Lit("abc").match("abc"))

    def test_match_partial(self):
        self.assertFalse(Lit("abc").match("abcdef"))

    def test_no_match(self):
        self.assertFalse(Lit("abc").match("xyz"))

    def test_empty_text(self):
        self.assertFalse(Lit("abc").match(""))

    def test_recursive_match(self):
        self.assertTrue(Lit("abc", Lit("def")).match("abcdef"))

    def test_recursive_no_match(self):
        self.assertFalse(Lit("abc", Lit("xyz")).match("abcdef"))

if __name__ == '__main__':
    unittest.main()
